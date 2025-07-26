
# Upload Templates

The `SelectFilesButtonTemplate` allows you to modify the **Select Files...** button. It lets you change the default text of the button and include custom content like an [icon](slug:common-features-icons) or image.

>caption Using Upload SelectFilesButtonTemplate

```RAZOR
    <TelerikUpload>
        <SelectFilesButtonTemplate>
            <TelerikSvgIcon Icon="@SvgIcon.Upload" />
            Click to Select Files for Upload
        </SelectFilesButtonTemplate>
    </TelerikUpload>
```

## See Also

* [Upload API](slug:Telerik.Blazor.Components.TelerikUpload)
* [Upload Overview](slug:upload-overview)
* [Upload Validation](slug:upload-validation)
* [Upload Events](slug:upload-events)