# -- pointer generator


i = 1
j = 1
n = len(summaries[i-1])
summf = open("output/RSummary_"+str(i)+".txt","w",encoding="utf-8")
for r, d, f in os.walk("Git/pointer-generator/pointer-generator-master/logs/myexperiment/decode_test_400maxenc_4beam_35mindec_100maxdec_ckpt-238410/decoded"):
    for file in f:
        if j > n:
            i += 1
            n = len(summaries[i-1])
            summf.close()
            summf = open("output/RSummary_"+str(i)+".txt","w",encoding="utf-8")
            j = 1
        rf = open(os.path.join(r,file),"r",encoding="utf-8")
        summf.writelines([l+"\n" for l in rf.readlines()])
        rf.close()
        j += 1
summf.close()
