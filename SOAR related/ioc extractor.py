# import iocextract
import re

text = """IOCs
Sender: yvonne.lorie@re-freshpr.com<mailto:yvonne.lorie@re-freshpr.com>
Domains:
news.newsmax.com
13.57.55.103
newsmax.com
64.135.21.3
kriptokilavuz.com

# """

# pattner = r"([(A-Za-z){1}_0-9-]{2,15}(\.[A-Za-z_0-9-]{2,15}))+"

pattern = r"([\w-]{2,15}(\.[\w-]{2,15})+)"
outputs = {}

domains = re.findall(pattern, text)
domains = [d[0] for d in domains if re.search('[a-zA-Z]', d[0])]
outputs["domain"]=[{"item": item} for item in domains]

print(f"found {len(domains)} domains")
# for i in domains:
#     if re.search('[a-zA-Z]', i[0]):
#         print(i[0])
#     else:
#         print(f"not domain : {i[0]}")

print(outputs)

# print(domains)