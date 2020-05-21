# %%writefile  gitBB2.py
## QQ-BAT
BB2 = {
"id_rsa" : "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQ0KTUlJRW93SUJBQUtDQVFFQTFJaDMzeFY2eTlqQmRJZ0J6Ty9PcFJvVkF3aVJEL1FQMEZDdlc4ZEtqYXMxdWlwdg0KQjZyQkczTFczWksrcXVBRWg5ZHFMejhqbjFYTEJNR2hNRktFVjZnMlJ0b2Z3c1c5NUpDNUU5UmVQOUpRREEwMA0KMVVGTURrTE15ejRkejczUXVEb0tpL3VSNEZwTkh3RFkwSGNvY2hpemN3RW5ncFkyRURxd2V0RGhUUGpSbTF0dA0KOFNRKzJ3M1oxckFjTnVsR2RDc1h2Y2svQ1hoQTRvRkFKdDIwdHNlbC8yUlpsNGxUNGo5WVhVS3ZsVlZscnZYRA0KNnRhc0tXNEFWMUgyVHF3ZU1jL0x2UE5VaEtiejVaMTlJWjQwRnRoYXBRYXhQVFl3NDcxK0JtUHZiRm1wUmFqKw0KQ3liUHJ0cWpTbkxlQXFBSnNJNisrU0VQNUhLUitYUnpCK3pXT1FJREFRQUJBb0lCQVFDWm1WY292dGxVWVg3Tw0KdlV5djA5QkF1aXpkV0YrZWJBRFJ5TDR6VWtDclNrVTJHbHpMNmJoT0loenZYWksyNDlmaVpPaTA1S2pXQ3FjQw0KOVAyTmN0VjZsSE5GbVhiQ3lTNkg5YUFNbUxyVTNTWkV6M2FUZVBHQ2pQeDlGcE50QS8zSVp3b2dTTndRakxLWA0KNllESWlKV09nQk9RMWhDNzY5dCt0eXU4VnlHOUFmUmtLNTBVdHhEMk85WkhaTC9IWG1RSy9LcGgzSGdjRkkwUg0KTExEc0JvVUxycjdGYTNodG5ndjhVeXZYd01rZXV0VWFnMVdKOERzODI5UUUwaXc3YUc2TXhvbmNsMVpWVUQ1Uw0Kb1ZSMmFqV1RUWjRHaGZKYkhJUGxNK2tDNUM5WGxPMGVRdDcxTWpmOUxFWjhVT0pFU3RRTFJBRnBiVkJORGcwdw0KbFpJUFhMZVJBb0dCQVBuenFEY1dmdEYvMUNIZkhJWklWdGZwSG5YUGY5Q1R1MGwySmp2blM4QTFtRTRUVVNiaw0KT0QzcWVUbXFMY0dpVlBYNVkwWXNJYU1KRkNGMFlwaVpYcHUwRkZZRlpFSmNKZTZJbUptYkREeW9KNE55bEtSTQ0KeVp6OEZPWnp1YnVkZk92bmdFTWdYVHRqM01Kckp5QUJqMFR6R0RMSjJhTnM4SlBJTitUVmhoeExBb0dCQU5tdA0KQkx4YXc2b0pQU2RGSEQrMkozdGJNMjdEeEZSUmtJMmcxc0hKQXB3dEJTdnN6RVp1OXBPaGcvWmlhamNCVUhPKw0Kc1lQcjNJSE5XNUxwTnV3QVRGcHgyMnZYYTRNZVBnWHVlcDBMNkJtUDFwcHNUTndZSlZNRHZtVDlNMk80QWptRA0KV0YralU5L3NHZHMwWlJFUG9aNk1WN2JQcVZvZTFSRFFlUmtrYTMwTEFvR0FYYkU5M3RocDFUSHJYSDc3ZkVKbA0KZXkyQkkzd1NWeWJwVDFJZ1p0ZitoeUFQNVVSTWFSMm5EMTV5N25DaUVqRTlVNjZWemRvQkNkSC9YOEwycW1qag0KRTg1ZXlSZmdTeGVyaUV4ZmwwU05RN2RzaUZOTThJRndHWTVNYjAzMTB5UG5qYTRMWUI0amxIMk1aTHd4d0VlVg0KWXEwVTV3VE90Zm5CL0VOUzRFNUJwUjBDZ1lBSjZ2SXVTc3hqY094U1g3bTd4V2JqSGZLbjkwOTRzQWF3RFVYNw0KcWxidUdyY0RtMVJyV1I3dTl3cjJMT0crQTlkUWpyMnp6d2xLK0xwVlpUN1ZYZVljc05kWWdJWXJnVE0rUGZGaw0KT21pbTBZRHJwRWVVTjUxcnZOM3Q2QU54WmE3a1EvSEEyY1kyaTZGWjlYY3RZZEx4VUYrbXVxdHlxYmozZlNnbg0KVnh0MnBRS0JnSDNTRjhXRzZxbnZ4bGJJTVhtQTUxRUgzMCtscFJZLzhzWUVYdjV5SWxQL2xXWW0yZldLemlLeA0KcHdSZmhyQXg0NGdqcEhlOHp3emhUcTY4d1RhNmdLcDZVTHlFRGY2MUd4UTVZUVpXUmcrYjdSZjViZmdaOWE2bQ0KYVpVZDVhK0V5b3Vac1dTY2U4anZRWUdaRCtNcnRRVTRzZVZ4WGxRTVV0aHRhaFZ1WU5GUQ0KLS0tLS1FTkQgUlNBIFBSSVZBVEUgS0VZLS0tLS0=",
"id_rsa_pub" : "c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFEbVJrTzFyVlJEMnRYaVFSYjBsSjN3LytGRWdFVldMRW5CZUlHYkpXOEwxVjV0bFo4Q2djdnJHYXQrQXJFanNCUTJZVnNldmJkMkw4ZzZ4Y0NtYXNIWFNaTFRVU21oSVQrVEZUOWd2d2haVU5ZbFZvdEpzR3pDb2ZpRlZhNHQ0YnBlbm1jeWQ0cnFkbzVNY0RybSswYWJaSk9lbUJ2S3M3bnpYdWpPTnpyMkhjeXZMKzVyclpGK2J3UmQ4aUFMMVlkTHc4WWc2Uk1jcVNZNXNpRUNCVFVucVBZcG5ZenZyQnhzbGE0MEpHbGFFa3N4ckNqK3NyYnF6ems1TGJJa0ZpdTFmdlRGZEJyMFluRXpjcEN3MnNVUTA1bjc2YlozQmpQTDdzamR1T2paR042dXhyckROT1RMeGZMVnpnY1dNYlZMbHBzdk1oeDE1ZWVoYzFldUxXQUogbG9naW4wNTE2bXA0QGdtYWlsLmNvbQ0K",
"known_hosts" : "Z2l0aHViLmNvbSwxNDAuODIuMTE0LjMgc3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBQkl3QUFBUUVBcTJBN2hSR21kbm05dFVEYk85SURTd0JLNlRiUWErUFhZUENQeTZyYlRyVHR3N1BIa2NjS3JwcDB5VmhwNUhkRUljS3I2cExsVkRCZk9MWDlRVXN5Q09WMHd6ZmpJSk5sR0VZc2RsTEppekhoYm4ybVVqdlNBSFFxWkVUWVA4MWVGekxRTm5QSHQ0RVZWVWg3VmZERVNVODRLZXptRDVRbFdwWExtdlUzMS95TWYrU2U4eGhIVHZLU0NaSUZJbVd3b0c2bWJVb1dmOW56cElvYVNqQit3ZXFxVVVtcGFhYXNYVmFsNzJKK1VYMkIrMlJQVzNSY1QwZU96UWdxbEpMM1JLclRKdmRzakUzSkVBdkdxM2xHSFNaWHkyOEczc2t1YTJTbVZpL3c0eUNFNmdiT0RxblRXbGc3K3dDNjA0eWRHWEE4VkppUzVhcDQzSlhpVUZGQWFRPT0xOTIuMzAuMjUzLjExMiBzc2gtcnNhIEFBQUFCM056YUMxeWMyRUFBQUFCSXdBQUFRRUFxMkE3aFJHbWRubTl0VURiTzlJRFN3Qks2VGJRYStQWFlQQ1B5NnJiVHJUdHc3UEhrY2NLcnBwMHlWaHA1SGRFSWNLcjZwTGxWREJmT0xYOVFVc3lDT1Ywd3pmaklKTmxHRVlzZGxMSml6SGhibjJtVWp2U0FIUXFaRVRZUDgxZUZ6TFFOblBIdDRFVlZVaDdWZkRFU1U4NEtlem1ENVFsV3BYTG12VTMxL3lNZitTZTh4aEhUdktTQ1pJRkltV3dvRzZtYlVvV2Y5bnpwSW9hU2pCK3dlcXFVVW1wYWFhc1hWYWw3MkorVVgyQisyUlBXM1JjVDBlT3pRZ3FsSkwzUktyVEp2ZHNqRTNKRUF2R3EzbEdIU1pYeTI4RzNza3VhMlNtVmkvdzR5Q0U2Z2JPRHFuVFdsZzcrd0M2MDR5ZEdYQThWSmlTNWFwNDNKWGlVRkZBYVE9PQo=",
"ALL" : ['id_rsa', 'id_rsa.pub', 'known_hosts']
}
# print('建立exe.py檔案')
##################################################################################################################################################################################################################
# from exe import BB2 
import os,base64,sys
##########################################
##########################################
cd = os.getcwd()
##########################################
hh = os.environ.get("HOME")
hs = os.environ.get("HOME")+"/.ssh"
##########################################
os.chdir( hh )
if not os.path.isdir(".ssh"):
    os.system("mkdir .ssh")
###########################
os.chdir( hs )
tmp = open('id_rsa', 'wb')
tmp.write(base64.b64decode( BB2.get('id_rsa') ))
tmp.close()
###########################
# ###########################
# tmpA = open('id_rsa.pub', 'wb')
# tmpA.write(base64.b64decode( BB2.get('id_rsa_pub') ))
# tmpA.close()
# ###########################

############# 權限不可以太高
os.system('chmod 600  '+hs+'/id_rsa')
os.system('ls -al $HOME/id_rsa')
os.system('ls -al '+hs+'/id_rsa')
################### 產生節點
os.system('ssh-keyscan gitlab.com >> '+hs+'/known_hosts')
os.system('ls -al $HOME/known_hosts')
os.system('ls -al '+hs+'/known_hosts')
################### 登入Git
os.system('ssh -T git@gitlab.com')
# print('執行完成!!'+sys.argv[1])
###############
###############
############### 個人資訊
os.system('git config --global user.name "moon-start"')
os.system('git config --global user.email "login0516mp4@gmail.com"')
###############
############### 
############### 回來 修改遠端位置
os.chdir(cd)
os.system("git remote set-url  origin   git@gitlab.com:moon-start/BAT-QQ.git")
os.system("git pull --rebase")
os.system("git add --all")
os.system('git commit -m "github-add"')
os.system("git push  origin  master:master -f")
