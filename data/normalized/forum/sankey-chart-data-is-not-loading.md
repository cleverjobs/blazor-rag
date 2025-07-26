# Sankey chart data is not loading

## Question

**Ana** asked on 10 Jul 2025

when i provide hardcoded data chart gets populated but on providing record from db the chart gets blank. this is my raozr page " <div class="row "> <div class="col-12"> <div id="chart-section" class="card chart-card"> <div class="card-body"> <div class="d-flex justify-content-between align-items-center mb-4"> <h5 class="card-title mb-0"> <i class="fas fa-project-diagram me-2 text-primary"></i> Deal Flow Analysis </h5> @* <div class="d-flex gap-2"> <button class="btn btn-sm btn-outline-primary"> <i class="fas fa-expand-arrows-alt"></i> </button> <button class="btn btn-sm btn-outline-primary"> <i class="fas fa-cog"></i> </button> </div> *@</div> <TelerikSankey Data="@Data"> <SankeyLinks ColorType="@SankeyLinksColorType.Static"></SankeyLinks> <SankeyLabels> <SankeyLabelsStroke Color="none"></SankeyLabelsStroke> </SankeyLabels> </TelerikSankey> </div> </div> </div> </div>" this is how i am binding my data " private void GenerateSankeyData() { if (hubspotDealStagesDtos==null || !hubspotDealStagesDtos.Any() || hubDealData==null) return; var newNodes=new SankeyDataNodes(); var newLinks=new SankeyDataLinks(); var orderedStages=hubspotDealStagesDtos.OrderBy(s=> s.DisplayOrder).ToList(); foreach (var stage in orderedStages) { newNodes.Add(new SankeyDataNode { Id=stage.HubspotId, Label=new SankeyDataNodeLabel { Text=stage.Label } }); } foreach (var group in hubDealData.GroupBy(x=> x.DealStage)) { if (!int.TryParse(group.Key.ToString(), out int validId)) continue; double value=selectedViewBy=="value" ? group.Sum(x=> x.Amount) : group.Count(); newLinks.Add(new SankeyDataLink { SourceId=0, TargetId=validId, Value=value }); } Data.Nodes.Clear(); Data.Links.Clear(); foreach (var node in newNodes) Data.Nodes.Add(node); foreach (var link in newLinks) Data.Links.Add(link); StateHasChanged(); }" need help in this regard

## Answer

**Dimo** answered on 14 Jul 2025

Hello Anas, If hubspotDealStagesDtos and hubDealData are populated asynchronously, then GenerateSankeyData() must be called after these collections already contain data. Otherwise the Sankey is expected to be blank. [https://blazorrepl.telerik.com/wJahPykM44K8K9yQ43](https://blazorrepl.telerik.com/wJahPykM44K8K9yQ43) Please note the potential need to reset the Data collection reference if the object is created empty and populated later. Another option is to render the Sankey component after its Data is available in the UI layer of the app. Regards, Dimo Progress Telerik

### Response

**Anas** commented on 14 Jul 2025

after some work around chart has been loading in that format. what could be the possible reason?

### Response

**Dimo** commented on 14 Jul 2025

Anas, this is the first time I see such an issue. Please send me an isolated runnable example with dummy data, which results in the observed UI.
