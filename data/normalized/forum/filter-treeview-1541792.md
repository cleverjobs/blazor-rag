# Filter TreeView

## Question

**Mar** asked on 04 Nov 2021

Hi I would like to make a better filter function for the TreeView. Some of the features I would like are. Expand all nodes that are found Highlight them Maybe only high light the text that are found Has any one created such a function?

### Response

**Marin Bratanov** commented on 06 Nov 2021

Martin, all of these are possible already: - expanding nodes can be done with the ExpandedField of the data right now, but a better way though a collection is coming through this enhancement - highlighting is possible through selection - highlighting certain text is an application-level feature that can be done with the item template Ultimately, all three are part of the business logic of the app and need to be implemented in the application code.
