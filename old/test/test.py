import PhotoScan
chunk = PhotoScan.app.document.activeChunk
for i in range (len(chunk.cameras)):
    chunk.cameras[i].frames[0].path = chunk.cameras[i].path.replace(".jpg", ".tiff")