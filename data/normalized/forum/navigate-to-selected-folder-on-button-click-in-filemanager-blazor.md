# Navigate to selected folder on button click in Filemanager blazor

## Question

**Tas** asked on 08 Apr 2025

Hi Team, Is there a way to programmatically navigate to selected folder on button click in Filemanager blazor

## Answer

**Anislav** answered on 08 Apr 2025

Yes, you can achieve this by tracking the selected items using the FileManager's selection feature ( docs ) and implementing a custom tool. When the user clicks your custom tool's button, you can access the selected item. If it's a directory, you can programmatically set the FileManager’s Path parameter ( docs ) to navigate into that folder. Keep in mind that users can select multiple files or folders by holding the Ctrl key and clicking, so make sure to handle that accordingly in your logic. Regards, Anislav Atanasov
