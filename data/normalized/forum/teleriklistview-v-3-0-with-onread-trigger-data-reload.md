# TelerikListView > V. 3.0 with OnRead, trigger data reload

## Question

**Jen** asked on 23 Jan 2022

Hi, I use ListView with attached OnRead event handler to page and filter data at database level. When the filter changed, I only called the read data event handler with the previously saved DataSourceRequest again which assigned the data to the bound list. Now I must use the eventargs properties, which is ok for paging but not for any other data-changing use case. There is no Grid State like feature in ListView and binding the Data property is forbidden when using OnRead (at least it has no effect). So, how to manually trigger OnRead in v3.0 ListView?

### Response

**Andy** commented on 25 Jan 2022

Same issue. I allow filtering on my parent component and need the ability to refresh the data.

### Response

**Ivan** commented on 26 Jan 2022

Same issue. How to fire OnRead for TelerikListView? Developers, is it difficult to answer the question? It's been three days already.

## Answer

**Hristian Stefanov** answered on 26 Jan 2022

Hi all, Currently, we are developing a method that will trigger the OnRead event of all components manually. It should be included in our next release 3.1 at the beginning of March. In the meantime, I can suggest a workaround. The ListView will fire OnRead in the following scenarios: change in Page value change in PageSize value change in Pageable value OnParameterSetAsync event (i.e. if you recreate the component) For example, you can toggle the PageSize value like this: @using Telerik.DataSource
@using Telerik.DataSource.Extensions <TelerikListView TItem="@SampleData" OnRead="@OnReadHandler" Pageable="true" PageSize="@PageSize"> <Template> <div class="listview-tile"> @context.Name </div> </Template> </TelerikListView> <p> <TelerikButton OnClick="@RebindListView"> Rebind ListView </TelerikButton> </p> <style>.listview-tile { display: inline-block; width: 100px; height: 100px; margin: 1em; border: 1px solid #ccc;
} </style> @code{
int PageSize { get; set; }=15;
bool ListViewRebindFlag { get; set; }
int CachedPage { get; set; }
string DataString { get; set; }="Initial data";

async Task OnReadHandler(ListViewReadEventArgs args)
{
// do not rebind during workaround algorithm
if (!ListViewRebindFlag)
{
// prevent Page index reset after workaround
if (CachedPage> 0)
{
args.Request.Page=CachedPage;
CachedPage=0;
}
var result=await GetListViewData(args.Request);
args.Data=result.Data;
args.Total=result.Total;
}
else
{
CachedPage=args.Request.Page;
}
}

async Task RebindListView()
{
// simulate new data
DataString="new data arrived";
GenerateData();

// workaround start

// trigger fake rebind
ListViewRebindFlag=true;
PageSize--;
// ensure that property value toggling takes effect
await Task.Delay(1);

// trigger actual rebind
ListViewRebindFlag=false;
PageSize++;

// workaround end
}

async Task <DataSourceResult> GetListViewData(DataSourceRequest request)
{
return AllData.ToDataSourceResult(request);
}

protected override void OnInitialized()
{
GenerateData();
base.OnInitialized();
}

void GenerateData()
{
AllData=Enumerable.Range(1, 500).Select(x=> new SampleData
{
Id=x,
Name=$"{DataString} {x}"
}).ToList();
}

List <SampleData> AllData { get; set; }

public class SampleData
{
public int Id { get; set; }
public string Name { get; set; }
}
} Regards, Hristian Stefanov

### Response

**Ivan** commented on 26 Jan 2022

Thank you!! Have you reproduced this workaround yourself? Go to the last page of the pager and click the RebindListView button The pager will remain on the last page, but the list will be from the first 15 objects.

### Response

**Andy** commented on 29 Jan 2022

Has anyone tried this fix yet? In general it works but occasionally it stops working unless it do something else to trigger the event. (like go to the next page)

### Response

**Hristian Stefanov** answered on 31 Jan 2022

Hi all, Thank you for noticing. There was indeed a problem with the suggested workaround. The Page value resets during the workaround procedure. As a result, the ListView requests items from page 1 in the second OnRead call during rebinding. That is why there is a need to cache the Page value and reapply it afterward. I apologize for the inconvenience. I also updated the code in my runnable example from the previous answer. Regards, Hristian Stefanov
