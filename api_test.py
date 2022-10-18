import requests

def set_url(string):
    return "http://localhost:4000/" + string

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


# def test_inputs():
#     response=requests.get(output_list[7])
#     print(response.text)

validate_200_status()

validate_missing()

print("\nTesting REST API on localhost:4000...\n")

print(*statcodes,sep='\n')
