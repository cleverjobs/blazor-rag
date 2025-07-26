# Unable to set initial value of the combobox in a grid

## Question

**Joh** asked on 26 Jan 2022

Hi, I'm quite new with telerik and I'm facing a probleme. A use the grid to follow the status of a property. These status is defined by an enum (it could have been a dictonary, anyway) When I bind my Grid datasource, in there is an int field representing the enum status. IE: 0=open, 1=Closed,... So I've bound the enum to the comboox, TextField and ValueField displays the correct data but on load for example, i'm not able to use the @bind-Value to the correct row. even more, on runtime, if I change one combobox, every comboboxes changes their value I don't see the solution <TelerikGrid Data="@WorkingData" Height="auto" Pageable="true" Sortable="true" PageSize=30 Resizable="true" EditMode="GridEditMode.Popup"> <GridColumns> <GridColumn Field="@(nameof(Work.Status))" Title="Status" Editable=true> <Template> <TelerikComboBox Width="100%" Data="@comboData" TextField="Value" ValueField="Key" @bind-Value="@cbValue"> </TelerikComboBox> </Template> </GridColumn> <GridColumn Field="@(nameof(Work.Comment))" Title="Comment" /> </GridColumns> </TelerikGrid> @code
{
enum TicketStatus
{
Open=0,
Close=1,
Planned=2,
Canceled=3
}
public class Work
{
public int Status { get; set; }
public string Comment { get; set; }
}

private List <Work> WorkingData;
private Dictionary<int, string> comboData;
private int cbValue;

protected override void OnInitialized()
{
base.OnInitialized();

comboData=Enum.GetValues(typeof(TicketStatus)).Cast <Enum> ().ToDictionary(t=> (int)(object)t, t=> t.ToString());

WorkingData=new List <Work> {
new Work{Status=1,Comment="My First property"},
new Work{Status=3,Comment="My second property"},
new Work{Status=2,Comment="My Third property"},
};

cbValue=0;

}
} Does anyonce could help me Regards;

## Answer

**Marin Bratanov** answered on 30 Jan 2022

Hello John, You need to use the template context to get the current value for the current row. The provided code will set all combos in all rows to the same 0 value. Also, if you want to edit data in the grid, use its built-in editing. Otherwise, while you will edit the current model, this will not travel to the real data source so the change will not actually be saved. If you want to keep using this approach, use the combo events (ValueChanged or OnChange) to update the database. Regards, Marin Bratanov

### Response

**John** commented on 04 Feb 2022

Thanks. By checking all the example, i've found some sample
