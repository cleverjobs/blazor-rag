# Close button misplaced

## Question

**EdEd** asked on 08 Dec 2020

Please see the attached image. I don't have any idea what caused this. I can't figure out how this could have happened. Can someone show me how to add some css to move the 'X' over a bit? Thanks ... Ed

## Answer

**Nadezhda Tacheva** answered on 09 Dec 2020

Hello Ed, In order to investigate further and clarify what is causing this appearance, we will need some more details or may be a code snippet showing your approach. In the meantime, you can style the selected elements by cascading through their parent element - the MultiSelect component. You can set a CSS class to the MultiSelect via its "Class" parameter. Then you will be able to style all the li tags in it (the li tags are holding the spans with the selected items). See the example below for reference: <style>.MyMultiSelect li{
width:auto;
} </style>

<TelerikMultiSelect Data="@Countries" @bind-Value="@Values" Placeholder="Enter Balkan country, e.g., Bulgaria" Width="350px" ClearButton="true" AutoClose="false" Class="MyMultiSelect">
</TelerikMultiSelect>

@if (Values.Count> 0 )
{
<ul>
@foreach ( var item in Values)
{
<li>@item</li>
}
</ul>
}

@code {
List<string> Countries { get; set; }=new List<string>();
List<string> Values { get; set; }=new List<string>(); protected override void OnInitialized ( ) {
Countries.Add( "Albania" );
Countries.Add( "Bosnia & Herzegovina" );
Countries.Add( "Bulgaria" );
Countries.Add( "Croatia" );
Countries.Add( "Kosovo" );
Countries.Add( "North Macedonia" );
Countries.Add( "Montenegro" );
Countries.Add( "Serbia" );
Countries.Add( "Slovenia" ); base.OnInitialized();
}
} Regards, Nadezhda
