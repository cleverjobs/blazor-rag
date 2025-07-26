# How to restrict file name with special characters at the time of uploading file using TelerikUpload control

## Question

**Ank** asked on 08 Jul 2021

I want to restrict file name with special characters at the time of uploading file in Dot Net blazer application using Telerik control. I am not finding any valid solution to validate file name, any specific solution for this. I know we can write validation related code in each individual method but I want common solution for all files where I have used TelerikUpload control. <TelerikUpload SaveUrl="@SaveUrl" RemoveUrl="@RemoveUrl" OnUpload="OnUploadEvent" OnRemove="@OnRemoveEvent" AllowedExtensions="@( new List<string>() { ".xlsx ", ".xlsm ", ".jpg ", ".jpeg " ,".doc " ,".docx ", ".pdf "} )" SaveField="files" RemoveField="fileToRemove"> </TelerikUpload>

## Answer

**Marin Bratanov** answered on 11 Jul 2021

Hi Ankush, You can use the OnSelect event and cancel it if the file selection does not satisfy the criteria you have: [https://docs.telerik.com/blazor-ui/components/upload/events#onselect.](https://docs.telerik.com/blazor-ui/components/upload/events#onselect.) If you want to make that part of form validation, see this sample project: [https://github.com/telerik/blazor-ui/tree/master/upload/form-validation](https://github.com/telerik/blazor-ui/tree/master/upload/form-validation) (note the readme file and how that is not yet available in the framework, so the validation logic must be implemented in the application code). Regards, Marin Bratanov Progress Telerik
