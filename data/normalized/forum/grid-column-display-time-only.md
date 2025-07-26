# Grid Column display time only

## Question

**Art** asked on 01 Sep 2020

Hi, I have a grid with StartTime column, the source object for the grid has a property DateTime I can handle this using Template and format the output of the DateTime, showing time only <GridColumn Field=@nameof(DtoRead.Shift.EndTime) Title="@LanguageContainer.Keys[" MasterDataEndTime"]" Editable="false" Width="@ColumnSize.S"> <Template> @((context as DtoRead.Shift).EndTime?.ToString(@"hh\:mm", System.Globalization.CultureInfo.CurrentCulture)) </Template> </GridColumn> when Grid is loaded with data, I have filter on top of this column and it shows DatePicker control I want to show a TimePicker instead... how to do this? I want to see time only and filter time only values Thanks, Artem

## Answer

**Marin Bratanov** answered on 01 Sep 2020

Hello Artem, I first suggest you review this article on properly setting the Field of the column so it can work with nested objects: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-bind-navigation-property-complex-object.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-bind-navigation-property-complex-object.) As for a TimePicker - at the moment you can do this through a FilterTemplate: [https://docs.telerik.com/blazor-ui/components/grid/templates/filter.](https://docs.telerik.com/blazor-ui/components/grid/templates/filter.) You can also Follow this enhancement that will provide a feature on the grid for such a switch: [https://feedback.telerik.com/blazor/1454076-filter-date-time-in-grid.](https://feedback.telerik.com/blazor/1454076-filter-date-time-in-grid.) You may also find interesting this one for easier formatting of data: [https://feedback.telerik.com/blazor/1451067-add-attribute-format-for-grid-column-to-apply-c-standard-formats.](https://feedback.telerik.com/blazor/1451067-add-attribute-format-for-grid-column-to-apply-c-standard-formats.) I've added your Vote for both of them on your behalf to raise their priority. Regards, Marin Bratanov

### Response

**Artem** answered on 01 Sep 2020

Hi Marin, thanks for this information, I will take a look. Another question, is there a possibility to remove filter from specific column? so for example I have FilterMode="@GridFilterMode.FilterRow" but I want some columns do not have any filters.. is this possible? Thanks, Artem

### Response

**Marin Bratanov** answered on 01 Sep 2020

Hi Artem, You can simply set the Filterable parameter of such columns to False. You can read more about the filtering behavior here and about the parameters a column offers here. Regards, Marin Bratanov

### Response

**Artem** answered on 01 Sep 2020

Thank you. That works.

### Response

**Artem** answered on 01 Sep 2020

Regarding the TimePicker for column filter, do you know when this feature will be available? Approx release date? Thanks, Artem

### Response

**Marin Bratanov** answered on 01 Sep 2020

Hello Artem, The best way to get status updates is to click the Follow button and you will receive emails when something changes. When we know the release in which a feature or a fix will be implemented, the portal page gets updated with its number and you will receive an email. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 02 May 2021

Hi Artem, There is a new feature request about changing the format more easily that you can Follow here, I've added your Vote for you. Regards, Marin Bratanov
