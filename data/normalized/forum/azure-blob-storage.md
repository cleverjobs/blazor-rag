# Azure Blob Storage

## Question

**Gre** asked on 12 Jun 2023

Do you have an example of how to use the FileManager to manage files stored in Azure Blob Storage?

## Answer

**Hristian Stefanov** answered on 15 Jun 2023

Hi Greg, The Blazor FileManager is completely decoupled from the physical file system. The component will list any files and folders that you provide via the component's Data parameter or via OnRead event handler. From this point of view - the FileManager can display blobs from an Azure storage, if you data-bind the component to such information. As a client-side UI component, it requires specific data to be bound with a specific model. The FileManager cannot directly correspond with Azure Blob storage or any other storage service (e.g., AWS S3). Every service requires specific API calls in order to work properly. What you can do to make the FileManager work with Azure is to tie up the backend service bound to the FileManager with the Azure service. Overall, making the component work for a specific storage service, will require a dedicated implementation. Additionally, I found a discussion on StackOverflow that can serve you as a starting point: How to get all files from a directory in Azure BLOB using ListBlobsSegmentedAsync. Based on the information provided above, we do not have an example specifically with Azure Blob Storage. This stems from the fact that the component is designed to be decoupled from the physical file system, and there are numerous storage solutions utilized by different developers that cannot be encompassed within a single sample. If we can assist with anything else, I would be glad. Regards, Hristian Stefanov

### Response

**Kisan Raja** commented on 18 Oct 2023

Hi Greg, I'm also trying to manage files stored in Azure blob storage using the Telerik FIleManager Component. Have you got a solution on how to achieve this? Thanks in advance.
