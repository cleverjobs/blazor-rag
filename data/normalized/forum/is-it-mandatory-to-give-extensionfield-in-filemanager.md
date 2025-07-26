# Is it mandatory to give "ExtensionField" in FileManager

## Question

**Tas** asked on 14 Apr 2025

Hi Team, I don't want to show filename extension while showing file in FileView. Can we do it? Is it mandatory to give "ExtensionField" in FileManager?

## Answer

**Anislav** answered on 14 Apr 2025

There is no built-in support in the FileManager for hiding file extensions. The FileManager uses the ExtensionField to determine the file extension, which is then used to generate the full name of the file and to select the appropriate icon for each file. As a workaround, you could try setting the ExtensionField to null or to a property in your model that does not contain a value. However, this currently results in an ArgumentNullException when the FileManager tries to calculate the full name of the first file. You may consider reporting this issue or requesting support for hiding extensions in a future version of the library through the Telerik Feedback Portal: [https://feedback.telerik.com/blazor?typeId=3](https://feedback.telerik.com/blazor?typeId=3) Regards, Anislav Atanasov
