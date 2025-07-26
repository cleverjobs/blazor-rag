# Scheduler Sticky Header on Page Scroll

## Question

**PauPau** asked on 07 May 2025

I'm working with the scheduler and I need the header to be sticky on the page, on scroll. Not just on the grid itself. When I scroll down, I need the header to stick to the top and when I scroll back up, it should go back to its original position. The original k-scheduler-header css is already sticky. How do I make it sticky on the page?

## Answer

**Hristian Stefanov** answered on 09 May 2025

Hi Pau, To make the Telerik Scheduler's header sticky across the whole page when scrolling, you can apply custom CSS styles to the header element. The styles below are just an example using sticky positioning—you’ll need to adjust them depending on your layout and where the scheduler sits on the page. This case is all about applying custom CSS to the specific elements you want to affect. Keep in mind, this is a general demonstration. <style>.k-scheduler-layout-flex.k-scheduler-head { position: fixed; top: 0; width: 100%; z-index: 1000; /* Ensure it's above other content */ }
</style> Regards, Hristian Stefanov Progress Telerik
