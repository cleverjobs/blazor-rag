# Remove some options of SortBy in Toolbar of File Manager in Blazor

## Question

**Tas** asked on 07 Apr 2025

Hi Team, I want to remove some options (like Date created, Date Modified, Size) of Sort By in Toolbar of File Manager in Blazor but I am unable to do it. Can you please help.

## Answer

**Anislav** answered on 07 Apr 2025

The built-in FileManagerToolBarSortTool does not offer a way to selectively remove specific sorting options such as Date Created, Date Modified, or Size. The recommended approach is to customize the toolbar as described here: Telerik FileManager Toolbar Configuration. You'll need to exclude both FileManagerToolBarSortTool and FileManagerToolBarSortDirectionTool from the default toolbar, and implement your own sorting logic and UI as needed. This will require some development effort, but currently, there’s no reliable workaround—attempting to hide options via CSS would affect all context menus globally, which is not ideal. Regards, Anislav Atanasov
