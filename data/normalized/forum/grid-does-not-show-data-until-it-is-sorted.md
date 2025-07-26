# Grid does not show data until it is sorted

## Question

**Sta** asked on 20 Nov 2020

just a basic list as a data source: public List<Feature> Features { get; set; }=new List<Feature>(); as simple as I can make the Grid: <TelerikGrid Data="@Features" Sortable="true"> <GridColumns> <GridColumn Field="Qty" /> </GridColumns> </TelerikGrid> And an event to add features: void AddFeature() { Features.Add(new Feature() { Qty=1 }); } I can add the features just fine, but nothing shows in the grid until I sort, then it is all there - what am I missing? 8.5.2

## Answer

**Nadezhda Tacheva** answered on 24 Nov 2020

Hello Stan, As far as I can see from your example, you are trying to make the Grid change/react to the change in the data fired by an external event. There are a couple of ways to achieve that, I will list below examples for both using your scenario. You can find more details in this article. ObservableCollection When dealing with ObservableCollection type, the Telerik components subscribe to its CollectionChanged event to update. This means that when collection is changed, the component (in this case Grid) is notified that it has to react to the corresponding event. @using System.Collections.ObjectModel <button @onclick="@AddFeature">Add</button>

<TelerikGrid Data="@Features" Sortable="true">
<GridColumns>
<GridColumn Field="Qty" />
</GridColumns>
</TelerikGrid>

@code{ public ObservableCollection <Feature> Features { get; set; }=new ObservableCollection <Feature>(); void AddFeature ( ) {
Features.Add( new Feature() { Qty=1 });
} public class Feature { public int Qty { get; set; }
}
} Refreshing data In this case the reaction in the component will happen as soon as it detects a change in the object received through the corresponding parameter. In this case this parameter is "Data". For complex data types, in you case List, you need to create a new reference for the view-model field when you want the component to update. That's the general way parameter changes propagate down to child components in Blazor <button @onclick="@AddFeature">Add</button>

<TelerikGrid Data="@Features" Sortable="true">
<GridColumns>
<GridColumn Field="Qty" />
</GridColumns>
</TelerikGrid>

@code{ public List <Feature> Features { get; set; }=new List<Feature>(); void AddFeature ( ) {
Features.Add( new Feature() { Qty=1 }); Features=new List<Feature>(Features); } public class Feature { public int Qty { get; set; }
}
} Regards, Nadezhda
