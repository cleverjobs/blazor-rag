
## Environment
<table>
<tbody>
<tr>
<td>Product</td>
<td>LoaderContainer for Blazor</td>
</tr>
</tbody>
</table>

## Description

When the page is longer than the viewport, the TelerikLoaderContainer is not always visible. It is displayed in the center of the page as a whole, not in the center of the browser's viewport. So, if the user is at the top or bottom of the page they won't see the loader animation.

How to display the LoaderContainer in the center of the viewport?

## Solution

Use custom CSS to override the LoaderContainer `position` style to `fixed`. This will center the component in respect to the whole page width.

In addition, you may also adjust the position of the inner container - the one that holds the text and the animation. Thus, you can center it in respect to the "main" element and not the whole page.

The example below demonstrates the suggested approach. Uncomment the second styles portion to see the difference.

````RAZOR
@* Center the LoaderContainer in the viewport *@

<style>
    .customized-loader-container.k-loader-container {
        position: fixed;
    }

    /* .customized-loader-container .k-loader-container-inner {
        left: 7%;
    }*/
</style>

<div style="height:2000px; background-color:beige;"> Some long div </div>

<TelerikLoaderContainer Class="customized-loader-container" Visible="true" Text="Please wait..." />
````

