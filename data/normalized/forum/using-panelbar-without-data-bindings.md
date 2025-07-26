# Using PanelBar without Data bindings?

## Question

**imw** asked on 03 Jan 2022

We would like to use the PanelBar but not with a datasounce but instead like kind of a TabStrip with all content defined in markup code and each panel just containing a Blazor component. But it seems like the PanelBar does not work without a data source strangely enough?

## Answer

**Nadezhda Tacheva** answered on 05 Jan 2022

Hi Patrik, You are right, the PanelBar indeed does not work without a data source as it is designed like so. A component that would serve to cover your desired scenario is called ExpansionPanel - it will allow you to define separate panels and it will use markup approach. As such component is not yet available in Telerik UI for Blazor, I opened a request for it in our public portal on your behalf - ExpansionPanel component. You may also take a look at its Kendo UI for Angular version to explore its behavior - ExpansionPanel Overview. I added your vote to the public request to increase its popularity as we are prioritizing the feature requests implementation based on the community interest and demand. As I opened the request on your behalf, you are subscribed and will receive email notifications when its status changes. This is the best way to keep in track with the progress of the component as once we know which release will contain its implementation, we will update its status in the
