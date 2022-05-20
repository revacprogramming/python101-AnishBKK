text = "X-DSPAM-Confidence:    0.8475"
l = text.find("0")
print(float(text[l:l+7]))