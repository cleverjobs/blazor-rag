# Basic Use ?

## Question

**Dea** asked on 09 Sep 2022

I have my Blazor app, based it off the Demo app that comes with VS. How does one integrate this loader control into the app? I have a number of pages in the app and some have a telerik btn and grid on it. I would like after the button is clicked for this loader to show while the grid gets its data from the server. When done then have this loader disappear. Then demo when running looks like what I want. just dont know where to stick stuff and how to turn on and off. the Grid and buttons are within divs within telerik layout control. HOw that helps. Thanks Deasun

### Response

**Dimo** commented on 13 Sep 2022

We have a similar demo with a Grid and a Loader Container. In general, you can show and hide the LoaderContainer at any time, as long as it doesn't happen in a method, which is blocking the UI thread.
