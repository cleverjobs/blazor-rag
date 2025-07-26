# Grid Columns order not working with foreach statement

## Question

**Leo** asked on 14 May 2021

Hi, I have created a grid where I have some fixed columns at the being, then I have a list interaction to create some columns, and then I have more two columns which I would like to keep at the end of the grid. But, it is rendering all columns insert in the "foreach" loop in the end. Here is my grid: <TelerikGrid Data=@TenantBillingList Sortable="true" Groupable="true" FilterMode="@GridFilterMode.FilterMenu" Pageable="true" PageSize="50" ShowColumnMenu="true"> <GridColumns> <GridColumn Field="@nameof(TenantBillingDto.TenantName)" FieldType="@(typeof(string))" Title="@L[" TenantBilling.TenantName "]"> <Template> <b> @((context as ExpandoObject).GetOrDefault(nameof(TenantBillingDto.TenantName))) </b> </Template> </GridColumn> <GridColumn Field="@nameof(TenantBillingDto.EditionName)" FieldType="@(typeof(string))" Title="@L[" TenantBilling.EditionName "]" /> <GridColumn Field="@nameof(TenantBillingDto.CountryCode)" FieldType="@(typeof(string))" Title="@L[" TenantBilling.CountryCode "]" /> <GridColumn Field="@nameof(TenantBillingDto.Currency)" FieldType="@(typeof(string))" Title="@L[" TenantBilling.Currency "]" /> <GridColumn Field="@nameof(TenantBillingDto.EditionCost)" FieldType="@(typeof(double))" Title="@L[" TenantBilling.EditionCost "]"> <Template> @(((context as ExpandoObject).GetOrDefault(nameof(TenantBillingDto.EditionCost)) as int?).GetValueOrDefault().ToString("N2")) </Template> </GridColumn> @foreach (var consumable in ConsumableList)
{ <GridColumn Field="@(nameof(TenantBillingConsumablesDetailsDto.ConsumableQty) + " _ " + consumable.Name )" FieldType="@(typeof(int))" Title="@(consumable.Name + " #")" /> <GridColumn Field="@(nameof(TenantBillingConsumablesDetailsDto.ConsumableCost) + " _ " + consumable.Name )" FieldType="@(typeof(double))" Title="@(consumable.Name + " $")"> <Template> @(((context as ExpandoObject).GetOrDefault(nameof(TenantBillingConsumablesDetailsDto.ConsumableCost) + "_" + consumable.Name) as double?).GetValueOrDefault().ToString("N2")) </Template> </GridColumn> } <GridColumn Field="@nameof(TenantBillingDto.ConsumableTotalCost)" FieldType="@(typeof(double))" Title="@L[" TenantBilling.ConsumableTotalCost "]"> <Template> @(((context as ExpandoObject).GetOrDefault(nameof(TenantBillingDto.BillTotalCost)) as double?).GetValueOrDefault().ToString("N2")) </Template> </GridColumn> <GridColumn Field="@nameof(TenantBillingDto.BillTotalCost)" FieldType="@(typeof(double))" Title="@L[" TenantBilling.BillTotalCost "]"> <Template> <b> @(((context as ExpandoObject).GetOrDefault(nameof(TenantBillingDto.BillTotalCost)) as double?).GetValueOrDefault().ToString("N2")) </b> </Template> </GridColumn> </GridColumns> </TelerikGrid> Here is the grid result. As you can see, the columns "Total Consumables" and "Total $" should be at the end, and not before my dynamic columns.

## Answer

**Hristian Stefanov** answered on 18 May 2021

Hi Leonardo, We have this knowledge base article for specifying grid columns position, with a detailed description of the scenario, and the ways to get the desired result. Thanks to your question we have extended it a little bit and anyone interested can get more information now. In short, this is the expected behavior because of the order in which the framework initializes components. All the parent components are initialized before their child components. Because of this framework behavior, the foreach loop inserts the columns at the end of your application. I hope this helps and if you have any other questions, please let me know. Regards, Hristian Stefanov Progress Telerik

### Response

**Leonardo** answered on 18 May 2021

Hi Hristian, Thank you for your answer. I managed to resolve the issue using the GetState and SetState methods. However, I was not able to do that in the events onStateInit and onStateChanged, I had to do that in the event onAfterRender when it is called after all columns are already added. Below my code to be able to change the order of the two columns. bool FirstReorder=true; protected override void OnAfterRender(bool firstRender) { var state=MainGrid.GetState(); if (state.ColumnStates.Count> 7 && FirstReorder) { FirstReorder=false; state.ColumnStates.Where(x=> x.Index==5).First().Index=998; state.ColumnStates.Where(x=> x.Index==6).First().Index=999; MainGrid.SetState(state); } } Could you please update the article to add an example for this scenario? It took me too much time to figured out a solution and I am not sure if it will work properly.

### Response

**Hristian Stefanov** answered on 21 May 2021

Hi Leonardo, There is an open feature request for Adding a Field property to the Grid's ColumnState. I have already given your vote there on your behalf, this way, the priority of the requested feature is increased, and we are tracking this interest. You can also click the "Follow" button to get notifications via email about the request status changes. The workaround for getting the field and position of the grid column is by using ColumnState object. Your example with the OnAfterRender method is good for a workaround too, and will do the work for you if you want to maintain it. Yes, it is a valid approach, and by maintaining it, I mean that I find it a little bit hard in some scenarios. For example, if you are adding new columns to the Grid, their indexes will change. After that, you will always need to change the indexes in the method. On every SaveState will break and will need changing. In case that you are not using the scenarios that I described, this approach will be even better for your app. I hope this helps and if you have any other questions, please let me know. Regards, Hristian Stefanov

### Response

**Michal** commented on 04 Jul 2023

Hello Hristian, do you have some tip how to deal with the "simplier" situation: - Lets have a grid(gHL), with FOREACH columns generated from own ColumnList on single page(A) - Lets change the ColumnList(like switching between views) in OnParametersAsync on the same page(A) - Lets reload data by calling await gHL.Rebind() OR gHL.SetStateAsync(null); in OnParametersAsync on the same page(A) what is ok? - content(data) are loaded ok whats the problem? - Columns are reoredered (which is not expected) What is the correct(and wokring) way, to "rebind/reload/refresh" grid with NEW columnset with EXACT order as it is generated in foreach.... Components version 4.3.0(prior versions has this effect too 4.x.x+) - Or how to completly "reinit" the grid? - trick with the "@key=@it.JmenoSys" doesnt have any effect(found somewhere else in the forum) - columns FieldNames are like "col1,col2,...col9999...." number/datatypes captions of columns differs with any new columnset.... - interesting part begins with "///!! here we go: thanks, here is the important part for idea: <TelerikGrid TItem="ExpandoObject" Pageable="true" @ref="gHL" Sortable="true" Resizable="true" Reorderable="false" Groupable="false" AutoGenerateColumns="false" PageSize="50" OnRead=@gHLReadItems> <GridAggregates> foreach (var it in .....)
{ <GridAggregate Field=@it.FldName FieldType=@it.FldType Aggregate="@GridAggregateType.Sum" /> } </GridAggregates> <GridColumns> <GridCheckboxColumn Visible=.... /> <GridCommandColumn Context="ctx" Visible=... /> ///!! here we go:
foreach (var it in GridDef.ColStore.Where(x=> x.Verejny==true).OrderBy(x=>x.c_int_ord))
{ <GridColumn @key=@it.JmenoSys Field=@it.FldName FieldType=@it.FldType Title=@it.VerejnyNazev ShowFilterCellButtons="false" Width=@it.cSirkaSestava DisplayFormat="@it.Maska" TextAlign=@it.cZarovnani> <FooterTemplate> @if (it.Sumovat==true)
{
@context.Sum
} </FooterTemplate> </GridColumn> } </GridColumns> </TelerikGrid> protected override async Task OnParametersSetAsync()
{
GridDef.ColStore=await LoadDefinitionFromSomeWhere(param x y z...)

///!! here we go: "how" to rebuild the grid
//gHL.Data=null;
//var st=gHL.GetState();st.ColumnStates=null;
/*
var s=gHL.GetState();
s.ColumnStates.Clear();
await gHL.SetStateAsync(s);
*/
await gHL.SetStateAsync(null);
//gHL.Rebind();
}

### Response

**Hristian Stefanov** commented on 07 Jul 2023

Hi Michal, Thank you for providing such detailed information describing the issue you're encountering. Upon reviewing it carefully, I can confirm that you are correctly refreshing the Grid via the " Rebind() " method. In order to better understand and address the issue, I have made attempts to replicate it by extensively testing various Grid configurations using the " @key " approach. However, with the " @key " approach, it seems that the columns are correctly ordered on my end. This suggests that there may be some details that I am missing from the actual project configuration, which will help me accurately reproduce the issue. Therefore, as the next step, can you please provide me with a small runnable sample that demonstrates the actual Grid structure and allows me to reproduce the error? To make it more convenient for you, you can utilize REPL instead of attaching a project. This approach will enable me to conduct a more comprehensive investigation using a configuration that closely resembles your actual environment. I eagerly await your response and greatly appreciate your cooperation in this matter. Kind Regards, Hristian

### Response

**Michal** commented on 07 Aug 2023

Hi Hristian, maybe i dont have the right skill, but in REPL is not possible to "simulate" OnParameterSetAsync (), or is? lets have: pageA/{IdOf_GridColumnsDefinition} 1. pageA/1 -- this is the FIRST INIT of the page, everything is ok 2. navigateto(or click on some navmenu item) 3. pageA/2 4. navigateto 5. pageA/1 -- here is the problem, if pageA/2 has "similar" columns at the different possitions .... ... . result of point 1 and 5 should be the same(column orders), but is not. keypoint is NOT to reload whole page, just go to the same page, same session, different param=OnParameterSetAsync() is called. Thanks for the tips.

### Response

**Yanislav** commented on 10 Aug 2023

Hello Michal, I have reviewed the discussion and the code snippets you've shared. I noticed that the columns are ordered using the following code: foreach ( var it in GridDef.ColStore.Where(x=> x.Verejny==true ).OrderBy(x=>x.c_int_ord)) Could you please confirm if the statement that filters and orders the columns returns a collection ordered in the same way as the columns are displayed? To assist you further, I attempted to reproduce the problem in a REPL example. Based on my understanding, the parameter from the URL of the page determines which columns should be displayed. To simulate this, I used a NumericTextBox to modify a numerical parameter, which I then used to filter a column's collection. In the replicated scenario, the columns are indeed ordered as returned from the OrderBy statement. However, the CommandColumn is positioned in front after the initial change of the columns. Is this behavior similar on your end? If so, I would like to recommend reviewing the following article: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-dynamic-columns-with-static](https://docs.telerik.com/blazor-ui/knowledge-base/grid-dynamic-columns-with-static) This article explains that it is necessary to specify a @key for the columns. While you mentioned trying to set the @key in your initial response, it seems that it didn't achieve the desired outcome. To address this, could you kindly confirm whether you specify a @key for the static columns? Additionally, were the keys the same each time the Grid is rendered? If not, the order of the columns might indeed vary. For your convenience, I have provided a modified version of the REPL example shared earlier, where a @key is specified for the static columns as well, ensuring the preservation of the order: [https://blazorrepl.telerik.com/QxOilOYq30Ida2J116](https://blazorrepl.telerik.com/QxOilOYq30Ida2J116) I hope you find this approach useful. Please give it a try and let me know if it resolves the issue or if you require further assistance.

### Response

**Michal** commented on 13 Aug 2023

Hi Yanislav, thanks for your preparations, we are going to be pretty close: 1 - yes, "order by" is how "user wants" to have the columns order from left to right 1,2,3,.... but final result is different than expected 2 - all "fixed/frozen/static" columns should be at the begining and "always" visible=its the most logic place=UX . Becaouse at the end you will be fighting with scrolling and frozen troubles. Iam also tested FIRST and LAST column to be frozen and static, but yes, after changing columns set, the LAST column become seccond(also not expected) ie.: A=frozen,1,2,3,4,B=frozen after columns change it was: A,B,1,2,3... 3 - yes, using the KEY values(but not random). Here is the REPL based on yours, thanks for that: [https://blazorrepl.telerik.com/QnOsFRFd18mbfpiy30](https://blazorrepl.telerik.com/QnOsFRFd18mbfpiy30) Simplified scenario, with "three sets of columns". 1) at the begining columns are: 1,2,3=OK 2) after changing to set 2 its: 4,1,2,3=OK=thanks to "weird" KEY value 3) after changing to set 3 its: 1,2,3=but it should be=3,1,2=key is also used, but as real key, not as index (2) There is no relations between the sets(imagine it as different tables), example is only simplified to 4 columns with "same datafield names" Questions and solutions Q1) - Can you confirm that KEY is not "a key", but it needs to be an exact kind of the "foreach position index"? Will this play well, when user can reorder columns and store/load it by GRID.SetState? Base foreach remains the same(its like base table structure and user can reorder it afterwards) Q2) - Or, is there some command ,to force whole grid "reinit" (act same as in first enter to the page) ? to eliminate similar troubles with aggregates=than keying should not be necessary. (like: grid.Dispose(), grid.Init()....) Have a nice day

### Response

**Hristian Stefanov** commented on 16 Aug 2023

Hi Michal, During my absence, my colleague Yanislav provided coverage, and now that I've returned, I've diligently reviewed the most recent correspondences. Based on my observations, it appears that my colleague's REPL sample functions accurately, even without necessitating the inclusion of the @key directive for each column. Notably, when the value is "1," the columns arrange themselves in descending order, while a different value triggers ascending order. This seems to cover the behavior you are after. Yet, despite thoroughly examining your latest message, I find myself still somewhat uncertain about the specific aspect of the aforementioned sample that requires refinement to align with your requirements entirely. Regrettably, the discussion extended longer than anticipated, and for any inconvenience caused by this, I apologize. My intention was to ensure a complete grasp of your objectives. I'm looking forward to your response, which I hope will provide additional insights into your actual goal. Your input is greatly valued, and I'm here to assist in any way possible. Kind Regards, Hristian

### Response

**Michal** commented on 16 Aug 2023

Hi Hristian, welcome back to the discussion. Questions still persist, "what is the proper and only way" to maintain column orders to be EXACT how it was "declared at razor markup"(take a look at my previous sample and problematic setup when switching between no 2 and 3.). IF the order of the declaration doesnt matter, so what is the correct way to maintain column orders AFTER switching columns set runtime? Q1) By the "@key", to act as an index?=so the order of the declaration doesnt matter, @key is the index? If yes, is that fully and correctly reflected in grid.setstate/getstate, or will this have lots of side efects? like messed ColumnsCollection and InitializedColumns OR Q2) if there is no way to maintan correct column order(Q1), when switching to the different set of the columns, is there a way to reinit whole grid on page? So grid should act the same way as reloading whole page. To get whole picture and much more unexpected behavior: Run my sample and switch between set 1-3 and 3 to 1, pay attention what is the order of columns at all sets=switching runtime but starting with 1. And take a look how are they declared and what is the @key at declaration. Is it correct and expected output?(from the point of declaration order, NO. From the point of @key value, i dont know) change public int CurrentValue { get; set; }=1; to public int CurrentValue { get; set; }=3; rerun the code, switch to no1, and now you will see, that the column orders are completly different than before. But it must be the SAME(between 1-3 and 3 to 1 changing runtime), so how to achive to be persistent no matter if is changed runtime at existing page, or first load or at any other event? Is it correct and expected output? (from the point of previous run, no, i dont have a clue what is happening and how to defined it else) Thanks

### Response

**Hristian Stefanov** commented on 21 Aug 2023

Hi Michal, Thank you for providing me with additional clarifications regarding the scenario. I thoroughly reviewed your last message, along with the accompanying video. Let me now address the remaining concern and propose a fitting solution. Regarding the query about maintaining column orders exactly as declared in the Razor markup, both approaches—utilizing keys and not using keys—are suitable. However, in scenarios involving dynamic addition or removal of columns, implementing a unique "@key" for each column proves more advantageous. This empowers the Grid to distinct column positions, and I can affirm that using keys does not yield any negative side effects on the Grid state. Solution Now, moving on to the solution for the current scenario, I reviewed the REPL sample you provided. It appears that the issue arising from column order switches is rooted in duplicate keys. Specifically, columns such as "fld 1" and "fld 4" share identical keys. For proper determination of column positions, each column must possess a distinct @key value. With this in mind, to achieve the desired behavior, I recommend either the adoption of unique keys or, alternatively, the omission of keys. Given that the current scenario doesn't involve dynamic column addition or removal, either approach will be effective. I have modified the code in both manners. Feel free to run and test them to observe the outcomes: Solution without keys - REPL link Solution with unique keys - REPL link Let me know if this aligns with your requirements. Kind Regards, Hristian
