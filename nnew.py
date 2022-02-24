import requests

payload = {}
headers = {
    'Authorization': 'Basic eTk4ODY5ODJAbW5zY29ycC5uZXQ6U2I5OCpwQFJESDNW',
    'Cookie': 'ak_bmsc=00F7C51E14EA33B6101F3199CC5A82B0~000000000000000000000000000000~YAAQZvzDF8M8fY19AQAA/194kw6rDqlgoflcJDqghxlwEYG7ZzRZ2fL5WzeIai0YFoB4ov3IyPeB4QbiVUIlpCAXVYEOzcMXGZJcJif1EaQ3leva0JeZFNJP+1h2BeGQHSUNKHA1SezCNZs+dmDOWTQrePE6tYZ/tcnzd9GLFtNGLh8pAKdjX0r7h2TTrYVeKd0W2B4WkKbdOalItQ6q1OgxevjldwOyRH8e35uJhKFXTWocgCmDy8tnMp5bCHjTG+sSEpDjBwuGaKuQ2nhzAQcyI6/y2lE69lmuTHVTYbECabiLx7QeRcdBFBA93Tgee9OwPhlbpvlIYgucPo1hSAnRxTL577nnQjzkjoQ4YZ4HOuCCWrKkl13MVgTKfvlGpi4IzQ==; JSESSIONID=B18839000404C0F44D666EF7EE11D1E0; atlassian.xsrf.token=BSMP-3NDP-M3AB-8R70_bedc6149bef5f603be95d32373d46f95c8a69cf9_lin'
}
out_file = open(r'D:\AutomationC4E/Jira_Release_dtl.csv', 'w')
out_file.write("ProjectID,sp,\n")
ja_list = open("D:\AutomationC4E\jpid.txt", "r")
project = ja_list.readlines()
# print(Lines)
for line in range(len(project)):
    print(project[line])
    url = 'https://jira.marksandspencer.app/rest/api/2/search?jql=labels=TechDebt%26cf[10002]>0%26project={}'.format(project[line])

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    issues = response.json()

    if (issues == []):
        print("Its empty list")

    else:

        # if issues is not None:
        for x in issues['issues']:
            if x['id'] is not None:
                ProjectID = x['id']
                sp = x['fields']['customfield_10002']
                ProjectID = str(ProjectID)
                sp = str(sp)
                ProjectID = ProjectID.encode('utf-8').decode('ascii', 'ignore')
                sp = sp.encode('utf-8').decode('ascii', 'ignore')
                print(ProjectID)
                print(sp)
                out_file.write("{},{}\n".format(ProjectID, sp))
            else:
                out_file.write("{},{}\n".format(ProjectID, 'None'))
    # else:
    #     print("None")
