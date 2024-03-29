
import ee
ee.Initialize()


base_asset_path = 'users/fhatangimana8595/Reclassified/'
new_asset_path = 'users/fhatangimana8595/Reclassified_new/'  # Change this to your desired path for saving reclassified images

# List of years for which you have classified images with specific naming
years = [
      'Reclassified_2017', 'Reclassified_2019'
]

# Loop through each year, load the image, reclassify it, and save it
for year in years:
    # Construct the full asset ID for the original and new image
    original_asset_id = base_asset_path + year
    new_asset_id = new_asset_path + year  # This is where the reclassified image will be saved
    
    # Load the image
    image = ee.Image(original_asset_id)
    
    # Reclassify the image
    reclassified_image = image.remap([0, 1, 2, 3, 4], [1, 1, 2, 3, 4])
    
    # Define export task
    task = ee.batch.Export.image.toAsset(
        image=reclassified_image,
        description='Reclassified_' + year,
        assetId=new_asset_id,
        scale=30,  # Set the scale if necessary, depends on your image resolution
        maxPixels=1e13
    )
    
    # Start the export task
    task.start()
    
    # Optionally, print a message to confirm the task has started
    print(f"Export task for {year} started, saving to: {new_asset_id}")
