
# DropZone Template

The DropZone allows you to customize the default rendering of its content by using a `Template`.

The `Template` is a `RenderFragment` and allows you to add whatever custom content is required such as simple text, HTML elements, or other components.

>caption Use Template to add custom content in the DropZone

````RAZOR
<TelerikDropZone Id="@DropZoneId">
    <Template>
        <TelerikSvgIcon Icon="@SvgIcon.FileAdd" />
        <span>Drop files here</span>
    </Template>
</TelerikDropZone>

<TelerikFileSelect DropZoneId="@DropZoneId"  />

@code {
    private string DropZoneId => "my-dropzone";
}
````

## See Also

* [Live Demo: Implementing the Blazor DropZone Template](https://demos.telerik.com/blazor-ui/dropzone/template)
