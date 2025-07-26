# How do I feed the map markers as appropiate?

## Question

**Dav** asked on 25 Feb 2024

Hi; I have an app that will have items that I want to put markers up for across the U.S. (and a few internationally). So say I have 50,000 of these items that need a marker - that's way too many. So how do I approach this? When it is zoomed in, then it will have say 10 - 100 markers so are there events on each scroll and zoom and from that I then give it additional markers? That would work when zoomed in. Then what is the best way to handle zooming out? Maybe figure out the 200 best matches and only show those? thanks - dave

## Answer

**Nadezhda Tacheva** answered on 26 Feb 2024

Hi David, The functionality that will be useful in such a scenario is called marker clustering and it will be available in a future version of the UI for Blazor Map. This feature will allow grouping the markers at specific zoom levels when they are too many to be displayed separately. I voted for the request on your behalf and you may follow it to keep track of its progress. Another potential option to handle the scenario is to fetch different sets of markers as the user zooms. For that purpose, you may handle the upcoming Zoom event to pass the relevant data to the Marker Layer. Regards, Nadezhda Tacheva Progress Telerik
