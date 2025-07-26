# How to make Draggable Window not have positional offset while page scrolls?

## Question

**Rev** asked on 21 Jun 2024

I have a basic Telerik Window that is draggable and the window is a child of a main section of a page. When I scroll [in that page section], the Window will stay perfectly in position in the viewport. I can drag the window, release it, then scroll and it is still fine. The issue arises when I attempt to drag the window in any direction while scrolling on the page. The cursor will separate from the window header but still continues to drag in parallel of the offset created by the scroll. How can I prevent this offset while scrolling and dragging at the same time so that the window will always stay in the viewport? I have attempted to utilize the ContainmentSelector property by creating an invisible overlay (high up in the component tree) that is fit to the viewport but this did not seem to work.
