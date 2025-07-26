# Is there a way to set the saved state of the TileLayout component before it is rendered?

## Question

**Jef** asked on 10 Jan 2025

RIght now I'm setting the state of the TileLayout component in the OnAfterRenderAsync() method. This results in the tiles first rendering in the default positions and then quickly switching around to the saved positions. I do a similar thing with the Grid component using the OnGridStateInit event. Unfortunately, the TileLayout component doesn't raise this event.

## Answer

**Tsvetomir** answered on 15 Jan 2025

Hello Jeffrey, To achieve the desired outcome without the described flicker between the default and saved state, you can utilize the following CSS approach. In short, the approach simulates the functionality of the StateInit event, by hiding the component until the required state is loaded. Define a string property that will hold the TileLayout CSS class. For example: private string TileLayoutClass { get; set; }="hidden-tile-layout"; Hide the TileLayout with the following CSS styles: .hidden-tile-layout { display: none;
} Use the OnAfterRenderAsync() method to check if the TileLayout is already rendered and get the desired (saved) state. After that set the state and display the TileLayout. protected override async Task OnAfterRenderAsync ( bool firstRender ) { // get the saved state from local storate/database var state=await LocalStorage.GetItem<TileLayoutState>(stateStorageKey); //check if the TileLayout is already rendered and saved state is available if (state !=null && TileLayoutRef !=null )
{ // Set the saved state TileLayoutRef.SetState(state); // Display the TileLayout with the appropriate state TileLayoutClass="";
}
} I hope this approach serves you well in continuing with your project. Regards, Tsvetomir Progress Telerik
