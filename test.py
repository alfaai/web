from sdxl import ImageGenerator

client = ImageGenerator()

#Parameters set to their default values
images = client.gen_image(prompt=
    "Vibrant, Headshot of a serene, meditating individual surrounded by soft, ambient lighting.",count=1, width=1024, height=1024, refine="expert_ensemble_refiner", scheduler="DDIM", guidance_scale=7.5, high_noise_frac=0.8, prompt_strength=0.8, num_inference_steps=50)
print(images)
