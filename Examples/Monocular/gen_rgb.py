import glob

file_list = glob.glob('SAMPLE_DSET/*.jpg')
txt_file = open("SAMPLE_DSET/rgb.txt", "a")
file_list.sort()

for file in file_list:
    timestamp = file[22:-4]
    print('Timestamp is: ', timestamp)
    print('File is: ', file[12:])
    txt_file.write(timestamp + ' ' + file[12:] + '\n')

txt_file.close()
print('RGB file has been written successfully')