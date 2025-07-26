# OnStateChanged called twice while filtering

## Question

**Iva** asked on 19 Dec 2020

Hello! Is it normal that the grid's OnStateChanged event gets called twice when filtering? Other actions, such as sorting, resizing, and reordering, call OnStateChanged once. I have an event handler that stores the state of the grid in local storage, and it's rather annoying that it gets called twice for no reason.

## Answer

**Nadezhda Tacheva** answered on 22 Dec 2020

Hi Ivan, Thank you for reaching out! Indeed the OnStateChanged is being called twice on filter. It is a known bug and you can Follow it here. I have added a vote on your behalf to increase its priority. In the meantime, you can click on the Follow button to receive email notifications on status changes (this is the best way to know when a bug is fixed. When we plan it for a certain release, we announce that information in the public
