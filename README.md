# MultiMailionaire
Script to send a mail and attached docs to multiple peaople listed in an Excel(.xlsx) file.

## Dependency Installation
Make sure you have the latest version of Python Interpreter installed
Then Run
```console
pip install pandas openpyxl python-dotenv 
```

## Adding Credentials
```console
git clone  https://github.com/Har-sh-arma/MultiMailionaire/  && cd MultiMailionaire
```
```console
copy .env.example .env
```
Then open the .env file and replace the corresponding values.

>### To generate the SENDERPASS
>Follow these [instructions](https://owlhowto.com/how-to-generate-an-app-password-on-gmail-for-smtp-on-linux/ "Get APP Password")
```env
#Credentials
SENDERMAIL="your@mail.id"
SENDERPASS="generatedAppPass"
```


## Try out a Demo

### Add and Remove any Mails in the A colummn() of mails.xlsx
![image](https://github.com/Har-sh-arma/MultiMailionaire/assets/90756795/0e50cb0f-c3d9-416b-b509-17ad33b33732)

### Edit the mail.txt
![image](https://github.com/Har-sh-arma/MultiMailionaire/assets/90756795/239fb92d-e3fd-494c-8a10-abcacda8866e)

### Run command

```console
py a.py abc.pdf cc.pdf
```

#### The General Form of the Command
```console
py a.py attatchment1 attatchment2 attatchment3 attatchment4 attatchment5 attatchment6 ....
