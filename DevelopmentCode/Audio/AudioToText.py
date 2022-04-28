""""
    This class will hold the code responsible for converting the audio file to a text file.
"""
#https://pythonbasics.org/transcribe-audio/
#pykaldi will probably be used 
# 
# TODO
# Neural network acoustic Model 
# Transaction Model
# Decoding graph
# Word Symbol Table
# 
# methord for transcribing the audio file
# method for saving the output to .txt file 
# method/class for ensuring the transcriber is trained 
# 
#

#Import the required libraries for transcribing the .txt from the audio file
from Kaldi.asr import NnetLatticeFasterRecognizer
from kaldi.decoder import LatticeFasterDecoderOptions
from Kaldi.nnet3 import NnetSimpleComputationOptions
from Kaldi.util.table import SequentialMetrixReader, CompactLatticeWriter

# Set the paths and read/write specifiers
'''
model_path = "models/aspire/final.mdl"
graph_path = "models/aspire/graph_pp/HCLG.fst"
symbols_path = "models/aspire/graph_pp/words.txt"
feats_rspec = ("ark:compute-mfcc-feats --config=models/aspire/conf/mfcc.conf "
               "scp:wav.scp ark:- |")
ivectors_rspec = (feats_rspec + "ivector-extract-online2 "
                  "--config=models/aspire/conf/ivector_extractor.conf "
                  "ark:spk2utt ark:- ark:- |")
lat_wspec = "ark:| gzip -c > lat.gz"
'''

# Instantiate the recognizer
'''
decoder_opts = LatticeFasterDecoderOptions()
decoder_opts.beam = 13
decoder_opts.max_active = 7000
decodable_opts = NnetSimpleComputationOptions()
decodable_opts.acoustic_scale = 1.0
decodable_opts.frame_subsampling_factor = 3
asr = NnetLatticeFasterRecognizer.from_files(
    model_path, graph_path, symbols_path,
    decoder_opts=decoder_opts, decodable_opts=decodable_opts)
'''

# Extract the features, decode and write output lattices
'''
with SequentialMatrixReader(feats_rspec) as feats_reader, \
     SequentialMatrixReader(ivectors_rspec) as ivectors_reader, \
     CompactLatticeWriter(lat_wspec) as lat_writer:
    for (fkey, feats), (ikey, ivectors) in zip(feats_reader, ivectors_reader):
        assert(fkey == ikey)
        out = asr.decode((feats, ivectors))
        print(fkey, out["text"])
        lat_writer[fkey] = out["lattice"]

'''