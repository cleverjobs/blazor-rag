# DropDownList TextField from combined properties

## Question

**Art** asked on 21 Aug 2020

Hi, I have a dropdownlist and I want to have a TextField as a combined value between two properties of the context I can do this using <ItemTemplate> and it works, but only when I click on dropdown and see the list, list has items with combined properties When I select one item from that list and list is closed, the selected text in drop down list is not combined, it shows only code in my case How can I show selected value as Item Template? Code ( Description ) <TelerikDropDownList Data="@Sites" ValueChanged="@( (int v)=> SiteValueChangedHandler(v) )" TextField="@nameof(Site.Code)" ValueField="@nameof(Site.SiteId)" DefaultText="@LanguageContainer.Keys[" All "]" Width="200px" Id="ddlSite"> <ItemTemplate> @( string.Concat((context as Site).Code, " (", (context as Site).Description, ")" )) </ItemTemplate> </TelerikDropDownList> Thanks, Artem

## Answer

**Marin Bratanov** answered on 22 Aug 2020

Hello Artem, The ValueTemplate lets you determine how the selected item renders: [https://docs.telerik.com/blazor-ui/components/dropdownlist/templates#value-template.](https://docs.telerik.com/blazor-ui/components/dropdownlist/templates#value-template.) Regards, Marin Bratanov

### Response

**Artem** answered on 24 Aug 2020

Hi Marin, I tried your example and it works. Thanks, Artem
