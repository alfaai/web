import replicate
import os

def sticker(prompt):
    input = {
        "prompt": prompt,
        "output_quality": 100,
        "width": 512,
        "height": 512,
    }

    output = replicate.run(
        "fofr/sticker-maker:4acb778eb059772225ec213948f0660867b2e03f277448f18cf1800b96a65a1a",
        input=input
    )[0]

    return output


def pulid(inp_img, prompt):
    input = {
        "prompt": prompt,
        "main_face_image": inp_img,
        "width": 1024,
        "height": 768,
        "num_samples": 1
    }

    output = replicate.run(
        "zsxkib/pulid:c169c3b8f6952cf895d043d7b56830b4e9a3e9409a026004e9efbd9da42912b4",
        input=input
    )[0]

    return output


def face_sticker(inp_img, prompt):

    if len(prompt) != 0:
        input = {
            "image": inp_img,
            "prompt": prompt,
            "prompt_strength": 4.5,
            "instant_id_strength": .7
        }
    else:
        input = {
            "image": inp_img,
            "prompt": "a person",
            "prompt_strength": 4.5,
            "instant_id_strength": .7
        }

    output = replicate.run(
        "fofr/face-to-sticker:764d4827ea159608a07cdde8ddf1c6000019627515eb02b6b449695fd547e5ef",
        input=input
    )[1]

    return output
