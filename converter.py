def dcm2nii(input_path, output_path):

    import pydicom as dcm
    import nibabel as nib
    import numpy as np
    import os
    
    result = np.empty((0,2), dtype=object)
    for fname in os.listdir(input_path):
        
        abs_path = os.path.join(input_path,fname)
        dcmf = dcm.read_file(abs_path)
        line = np.array([[float(dcmf.SliceLocation), np.array(dcmf.pixel_array)]])
        result = np.append(result, line, axis = 0)
        
    result = sorted(result,key = lambda result:result[0])
    
    
    data = []
    for img in result:
        data.append(img[1])
    data = np.array(data)
    
    img = nib.Nifti2Image(data,np.eye(4))
    fname = os.path.join(output_path,input_path.split('/')[-1]+'.nii.gz')
    img.to_filename(fname)
        
    print('[info] file saved to', fname)