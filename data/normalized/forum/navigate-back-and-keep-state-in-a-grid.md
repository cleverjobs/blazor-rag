# Navigate back and keep state in a grid

## Question

**Mar** asked on 25 Nov 2021

Hi, I have a list of around 200 items. When you double click on a item you are taken to another page with a list of sub items. This is a read only app, no updates and I need it to be as fast a possible. Fetching data is fast around 30ms. I would like the main list (Telerik Grid) to keep it state including selected row, sorting and everything. This should work with the browsers back button and the blazor navigation manager. I was thinking of cashing the data, but it's the redraw that's taking time. Should this has been a server app?

## Answer

**Marin Bratanov** answered on 25 Nov 2021

Hi Martin , You can use the grid events - OnStateChange and OnStateInit to respectively save and load the grid state. You can read more about what the grid state can let you do (there is much more than that) in this article (which also has a section dedicated to saving and loading the state): [https://docs.telerik.com/blazor-ui/components/grid/state.](https://docs.telerik.com/blazor-ui/components/grid/state.) Regards, Marin Bratanov

### Response

**Martin Herløv** commented on 25 Nov 2021

thanks. I am already saving and loading state. I am looking for a way to avoid rerender the grid when I navigate back. are there any performance tips you can give me for a read only grid. I have set all fields to readonly but don’t see any performance gains

### Response

**Marin Bratanov** commented on 29 Nov 2021

The grid must always render because it will initialize anew after navigation. This is how any Blazor component will work - if it has been disposed, it will re-render. With the grid, even if you don't dispose it somehow (e.g., implement some trickery with the navigation and where in the layout hierarchy the grid is), perhpas you could avoid some re-renders by avoiding re-initialization. If you will need to restore its State, it will have to re-render. As for a readonly grid - this is a usability setting and it will not affect the rendering performance. Functionality related to editing is rendered when needed only. Thus, if you want a read only grid - if you don't intend to use other functionality a grid provides - perhaps a basic foreach loop and a plain <table> will render faster.
