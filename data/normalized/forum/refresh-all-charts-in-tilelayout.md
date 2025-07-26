# Refresh all Charts in TileLayout

## Question

**Nik** asked on 02 Jun 2021

Hello, Is there a way to refresh all Charts in a TileLayout without doing it on every Chart? My TileLayout is created dynamically, and I can have 1 or many Charts in it, but I want to refresh all of them on resize. I have a method that triggers when a user presses some key combinations, and then every Chart should do .refresh(). Thanks BR, Nikolas

## Answer

**Svetoslav Dimitrov** answered on 07 Jun 2021

Hello Nikolas, Firstly, I would like to make a quick summary of the scenario to make sure I understand the scenario correctly: You are generating the tiles of the TileLayout in a loop In the content of some tiles, you have the Chart component. You have provided a reference to every Chart that is present in the tiles. What I could suggest is that you create a collection of all Chart references: List<TelerikChart> ChartReferences { get; set; }=new List<TelerikChart>()
{ //references go here }; and on the OnResize event that the TileLayout exposes to loop through the ChartReferences collection and use the reference.Refresh method. Let me know if I misunderstood the question or if that solution works for your application. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Nikolas** commented on 07 Jun 2021

Hello Svetoslav, Perfect, thanks. I did that, but didn't know if there was another way, so would just check. But this works perfectly, thanks :) BR, Nikolas
