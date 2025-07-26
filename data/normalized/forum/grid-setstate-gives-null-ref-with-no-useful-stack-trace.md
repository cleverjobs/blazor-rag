# Grid.SetState gives null ref with no useful stack trace

## Question

**Jas** asked on 18 Feb 2022

I'm suddenly getting null refs when I call Grid.SetState and I need more information on why. User clicks Reset button: await Grid.SetState(null); And then I set a Default Sort var desiredState=new GridState <SearchDocumentItem> ()
{
SortDescriptors=new List <SortDescriptor> ()
{
new SortDescriptor { Member=member, SortDirection=dir }
}
};

if (Grid !=null)
await Grid.SetState(desiredState);

### Response

**Marin Bratanov** commented on 20 Feb 2022

Please add the error stack trace and when that issue happens.
