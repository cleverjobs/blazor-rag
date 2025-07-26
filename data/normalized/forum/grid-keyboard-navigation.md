# Grid keyboard navigation

## Question

**Pau** asked on 23 May 2022

Hi [http://https://demos.telerik.com/blazor-ui/grid/editing-incell](http://https://demos.telerik.com/blazor-ui/grid/editing-incell) demo's incell editing, I noticed that with Ctrl+Enter I can navigate one row down after editing. I wonder if the editboxes in the grid where not checkboxes (iusing the up and down arrow) I could use the arrow up and down to do the same? Eric

### Response

**Marin Bratanov** commented on 24 May 2022

Hi Eric, I would have to say that I feel like they couldn't - the arrow keys have an important meaning and use in numeric editors, and also in a multiline textarea editors, and they should also let you scroll. Perhaps what you are looking for in terms of UX is a spreadsheet component, and not a grid.
