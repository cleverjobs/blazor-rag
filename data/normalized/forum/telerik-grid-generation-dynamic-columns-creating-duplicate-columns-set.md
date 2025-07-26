# Telerik Grid Generation Dynamic columns creating duplicate columns set.

## Question

**Jit** asked on 08 Jul 2022

Hello I am trying to generate Dynamic columns for Telerik Grid it is generating multiple times columns set I want to avoid this please check bellow screen short. Here is the my code. <TelerikGrid Data="@SearchConfigs" Resizable="true" Reorderable="true" Groupable="false"> <GridColumns> @foreach (SearchConfig row in SearchConfigs)
{
@foreach (var property in (IDictionary<string, string>)row.SearchFields)
{ <GridColumn Title="@property.Key"> <Template> @property.Value </Template> </GridColumn> }
} </GridColumns> </TelerikGrid> public List <SearchConfig> SearchConfigs { get; set; }=new List<SearchConfig>();

IDictionary<string, string> keyValuePairs=new Dictionary<string, string>
{
{ "Col1", "Value1" },
{ "Col2", "Value2" },
{ "Col3", "Value3" },
{ "Col4", "Value4" },
{ "Col5", "Value5" },
{ "Col6", "Value6" },
{ "Col7", "Value7" },
{ "Col8", "Value8" },
};

SearchConfigs.Add( new SearchConfig { SearchFields=keyValuePairs });
SearchConfigs.Add( new SearchConfig { SearchFields=keyValuePairs });
SearchConfigs.Add( new SearchConfig { SearchFields=keyValuePairs }); Could you please help me figure out what is going wrong here? Thank you

## Answer

**Jitendra** answered on 08 Jul 2022

Here Is my answer I get it working <TelerikGrid Data=" @Data " Resizable=" true " Reorderable=" true " Groupable=" false "> <GridColumns> @if (Data !=null && Data. Any ())
{ // this sample uses the first data item to create columns for all keys present in it // which assumes all items have the same keys in them. If this is not your case // you may want to create your own list of column descriptors or any other logic to define the columns var firstItem=LocalData. First (); var dictionaryItem=( IDictionary <string, object>) firstItem; var fields=dictionaryItem.Keys; foreach ( var item in dictionaryItem )
{ if ( item.Key. Contains ( "IsActive" ))
{ <GridCommandColumn Width=" 120px " Locked=" true " Title=" View Logs "> <GridCommandButton Command=" DetailCommand " OnClick=" @DetailCommand_Clicked " ThemeColor=" @ThemeConstants. Button. ThemeColor.Primary " Size=" @ThemeConstants. Button. Size.Small " FillMode=" @ThemeConstants. Button. FillMode.Flat "> <span class=" k-badge k-badge-md k-badge-solid k-badge-rounded k-badge-primary "> Detail </span> </GridCommandButton> </GridCommandColumn> } else { <GridColumn Field=" @item.Key " FieldType=" @item.Value. GetType () "> </GridColumn> }
}
} </GridColumns> </TelerikGrid>
