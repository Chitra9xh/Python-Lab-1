def build_pc_config(**components):
    print("PC Configuration:")
    for k,v in components.items(): print(k,":",v)

build_pc_config(cpu="i7",ram="16GB",storage="1TB SSD")
build_pc_config(cpu="Ryzen 5",graphics_card="RTX 4060",ram="32GB",storage="2TB SSD",psu="750W")
