import requests

url = input("Enter a URL in the format 'http://x.x.x.x:4000/': ")

def set_url(string):
    return url + string

input_list = [
    "md5/test", 
    "md5/hello world", 
    "md5",
    "factorial/4",
    "factorial/5",
    "factorial/test",
    "factorial/0",
    "fibonacci/8",
    "fibonacci/35",
    "fibonacci/1",
    "fibonacci/test",
    "is-prime/1",
    "is-prime/2",
    "is-prime/5",
    "is-prime/6",
    "is-prime/15",
    "is-prime/37",
    "is-prime/one",
    "slack-alert/test",
    "slack-alert/This is a test" 
    ]

output_list = list(map(set_url, input_list))

statcodes = []

emoji_pass = "\U0001F197" 

emoji_fail = "\U0001F6D1"

line_break = "\n"

def collect_statcodes(url):
  for i in url:
    response=requests.get(i)
    statcodes.append(response.status_code)

collect_statcodes(output_list)

def validate_200_status():
    for i in [0, 1, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19]:
        if statcodes[i] == 200:
            statcodes[i] = f"{'* [GET]': <10}{str(input_list[i]): ^15}{emoji_pass: >10}"
        else:
            statcodes[i] = f"{'* [GET]': <10}{str(input_list[i]): ^15}{emoji_fail : >10}{line_break + ' - Expected HTTP Status: 200': >10}{line_break + ' - Actual HTTP Status: ' + str(statcodes[i]): >10}"

def validate_missing():
    for i in [2, 5, 10, 17]:
        if statcodes[i] == 400 or 404 or 405:
            statcodes[i] = f"{'* [GET]': <10}{str(input_list[i]): ^15}{emoji_pass: >10}"
        else:
            statcodes[i] = f"{'* [GET]': <10}{str(input_list[i]): ^15}{emoji_fail : >10}{line_break + ' - Expected HTTP Status: [400, 404, 405]': >10}{line_break + ' - Actual HTTP Status: ' + str(statcodes[i]): >10}"

def test_fib8():
    a = [0, 1, 1, 2, 3, 5, 8]
    r = requests.get(output_list[7])
    d = r.json()
    if a == d['output']:
         statcodes[7] = f"{'* [GET]': <10}{str(input_list[7]): ^15}{emoji_pass: >10}"
    else:
        statcodes[7] = f"{'* [GET]': <10}{str(input_list[7]): ^15}{emoji_fail : >10}{line_break + ' - Expected output: ' + str(a): >10}{line_break + ' - Actual output: ' + str(d['output']): >10}"

def test_fib35():
    a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    r = requests.get(output_list[8])
    d = r.json()
    if a == d['output']:
         statcodes[8] = f"{'* [GET]': <10}{str(input_list[8]): ^15}{emoji_pass: >10}"
    else:
        statcodes[8] = f"{'* [GET]': <10}{str(input_list[8]): ^15}{emoji_fail : >10}{line_break + ' - Expected output: ' + str(a): >10}{line_break + ' - Actual output: ' + str(d['output']): >10}"

def test_fib1():
    a = [0, 1, 1]
    r = requests.get(output_list[9])
    d = r.json()
    if a == d['output']:
         statcodes[9] = f"{'* [GET]': <10}{str(input_list[9]): ^15}{emoji_pass: >10}"
    else:
        statcodes[9] = f"{'* [GET]': <10}{str(input_list[9]): ^15}{emoji_fail : >10}{line_break + ' - Expected output: ' + str(a): >10}{line_break + ' - Actual output: ' + str(d['output']): >10}"

print(f"{line_break}Testing REST API on {url}...{line_break}")

validate_200_status()

validate_missing()

test_fib8()

test_fib35()

test_fib1()

print(*statcodes,sep='\n')
