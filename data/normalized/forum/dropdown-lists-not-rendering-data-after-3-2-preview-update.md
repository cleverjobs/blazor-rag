# Dropdown lists not rendering data after 3.2 preview update

## Question

**Jam** asked on 18 Feb 2020

So I'm experiencing something quite strange, where I have dropdown lists which I pre-populate with static values, those render correctly. But when I fill them with a list from an API, they no longer render anything. It just says "NO DATA"... This was working before the update. Furthermore, I've added a button which calls StateHasChanged but that doesn't resolve anything unfortunately And, I've console written the data the dropdown list should render, and the data is there.

## Answer

**Marin Bratanov** answered on 20 Feb 2020

For anyone else finding this thread, we have been working with James in a private ticket and I will paste here the summary. It looks like the data is created dynamically by using .Add() on an already existing list. This is expected to not update properly, you should use an ObservableCollection for this. Once outlier case that works was because the reference of the Data object changes (similarly to what new List<T>() would do). Here's an example of what I an referring to - the first one will not have data in the dropdown, and this is expected: @using System.Collections.ObjectModel

<TelerikDropDownList Data="@broken" @bind-Value="@brokenValue" />
<br />
<TelerikDropDownList Data="@working" @bind-Value="@workingValue" />

@code{
List<string> broken { get; set; }=new List<string>();
ObservableCollection<string> working { get; set; }=new ObservableCollection<string>(); string brokenValue { get; set; } string workingValue { get; set; } protected override async Task OnInitializedAsync ( ) { await GetData();
} async Task GetData ( ) { await Task.Delay( 500 ); //simulate network delay for ( int i=0; i <5; i++)
{ string item=$"item {i} ";
broken.Add(item);
working.Add(item);
}
}
} If, however, you change the data collection reference, the data will "show up": async Task GetData ( ) { await Task.Delay( 500 ); //simulate network delay for ( int i=0; i <5; i++)
{ string item=$"item {i} ";
broken.Add(item);
working.Add(item);
} //creating a new reference calls the OnParametersSet of the component whose parameter you touch //in this case the first DropDownList so it re-renderes and you see the data broken=new List<string>(broken);
} In some previous versions of our components (maybe up until 2.5.0 or 2.6.0) the "broken" example might have worked. It was never supposed to and that is the side effect of a bug which caused our components to re-render unnecesarily. This may be leaving an impression that it worked before, while it had been exploiting a bug. Regards, Marin Bratanov

### Response

**James** answered on 20 Feb 2020

Hi all, can confirm that my issue was resolved after converting my List to an ObservableCollection Ie: Convert: public List<ClassName> ListName=new List<ClassName>(); To: public ObservableCollection<ClassName> ListName=new ObservableCollection<ClassName>(); Thanks Marin!
