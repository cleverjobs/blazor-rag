# Blazor DataGrid scroll event

## Question

**Oli** asked on 18 Apr 2023

Hi, I'm looking to subscribe to scrolling events in the data grid using JavaScript. I've tried subscribing to the scroll event on the .k-grid and .k-grid-content elements, but the events don't happen Is there a way to do this? Thanks, Oliver

## Answer

**Svetoslav Dimitrov** answered on 21 Apr 2023

Hello Oliver, I am happy to report that it is possible to use JavaScript to subscribe to the scroll event. The target element must be the k-grid-content. Here is the JavaScript I used to subscribe to the scroll event: let targetElement=document.querySelector( ".k-grid-content" );

targetElement.addEventListener( 'scroll', ( event )=> { console.log( "grid scrolling" );
}); Regards, Svetoslav Dimitrov Progress Telerik
