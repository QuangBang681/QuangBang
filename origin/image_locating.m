function[z_image] = image_locating(z,depth)
z_image = -z-2*depth*ones(1,2);