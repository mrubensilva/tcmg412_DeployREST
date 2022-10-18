import requests

def set_url(string):
    return "http://localhost:4000/" + string

input_list = [
    "md5/test", 
    "md5/hello%20world", 
    "md5",
    "factorial/4",
    "factorial/5"
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
    "is-prime/one" 
    ]

output_list = list(map(set_url, input_list))

statcodes = []

def collect_statcodes(url):
  for x in url:
    response=requests.get(x)
    statcodes.append(response.status_code)
    # print(f"{'* [GET]': <10}{x: ^15}{response.status_code: >10}")

collect_statcodes(output_list)

print(statcodes)

print(statcodes[2])

# print(response.text)
