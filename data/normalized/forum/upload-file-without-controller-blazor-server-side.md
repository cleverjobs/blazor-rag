# Upload File without Controller (Blazor Server Side)

## Question

**Bes** asked on 15 Dec 2021

Hi I have a question about the Upload Component. Is it possible to Upload without using a controller? I have a referenced dll that can handle the Data and pass also the Files directly, without going through a controller?! Is there a way to achieve this? Thanks in Advance Best Regards Besir

## Answer

**Marin Bratanov** answered on 16 Dec 2021

Hi, The component for that in Blazor would be called a FileSelect, and you can Follow its implementation here: [https://feedback.telerik.com/blazor/1460649-fileselect-component](https://feedback.telerik.com/blazor/1460649-fileselect-component) (in the thread there is also guidance on how you can implement your own right now if you cannot wait for a month or so until it is available). Regards, Marin Bratanov
