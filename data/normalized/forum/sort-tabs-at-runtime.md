# Sort tabs at runtime

## Question

**Fab** asked on 28 Jul 2022

Hello, We need to let the user sort the tabs as they wish. These tabs are generated at runtime in a loop, is it possible to change the tab order once they are generated at runtime? Thanks

### Response

**Marin Bratanov** commented on 28 Jul 2022

Updating the collection reference to a new collection with the desired order should re-render the component. The important thing is to let the framework know to re-render (hence, the reference change you may need as this is a collection).
