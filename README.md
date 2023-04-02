# Spring-Hack-PSU
Project for Spring Hack PSU 2023 for Team Mustang. 

## Inspiration 
Incorporating American Sign Language (ASL) in banking can help banks become more connected to the deaf and hard of hearing community. By offering ASL interpretation services, banks can demonstrate their commitment to inclusivity and accessibility for all customers, including those with hearing impairments. This approach can lead to better relationships with the community, increased trust, and improved customer satisfaction. Ultimately, incorporating ASL in banking can help bridge the communication gap and build stronger connections with a diverse range of customers.

## What it does 
An ASL interpretation module can be a valuable tool for individuals in the deaf and hard of hearing community as it facilitates communication by interpreting ASL language and converting it into text in the form of proper sentences. By recognising and interpreting complex hand gestures and movements, this project can provide accurate translations of ASL signs and expressions into written language, allowing individuals who are not familiar with ASL to understand and respond appropriately.

## How we built it
In developing an ASL interpretation module, various tools and technologies were utilized to accurately track and interpret hand gestures and movements. The webcam video was first transformed into RGB, and then disturbances in the photograph were removed using specialized software. With the use of numpy and matplotlib, the index positions of the fingers were identified and tracked accordingly.

To determine the accuracy of the signs formed, NPM was utilized. In addition, the edges of the hand gestures were identified and tracked using the TensorFlow framework. The development of the ASL interpretation module was facilitated through the use of next.js and pyqt5 to create a functional and user-friendly website.

In summary, a range of tools and technologies were utilized in the development of the ASL interpretation module, including specialized software to remove disturbances in photographs, numpy and matplotlib to track finger positions, NPM to assess sign accuracy, snkLearn's Random Forest Identifier to identify and track hand gesture edges, and next.js and pyqt5 to create the website. By leveraging these tools and technologies, a functional and reliable ASL interpretation module was developed to facilitate communication between the deaf and hard of hearing community and the broader population.
## Challenges we ran into
The complexity of Understanding ASL . To make a module that can understand the hand gestures a person does and then converting those gestures to return a coherent text in real time 

## Accomplishments that we're proud of
One of our major accomplishments in developing an ASL interpretation module is the successful training of a CNN model from scratch to recognise and identify ASL symbols through hand gestures captured in live video feeds, which can then be accurately converted into text. This achievement required extensive data collection and labelling to create a comprehensive and diverse dataset that could be used to train the model.

Training the CNN model involved utilising a supervised learning approach, where labeled data was used to teach the model to recognise specific ASL symbols and their corresponding text. The model was trained to identify and distinguish various hand gestures, including finger positioning, hand shape, and orientation, to accurately interpret the meaning behind the ASL signs.

The successful training of a CNN model for ASL interpretation is a significant accomplishment that required considerable technical expertise, specialised equipment, and resources. Our team is proud of this achievement as it represents a significant step forward in developing an effective ASL interpretation module that can enhance communication and accessibility for individuals who use ASL as their primary mode of communication.

## What we learned
Our development of an ASL interpretation module provided an opportunity to learn and acquire valuable technical skills. One of the key skills we learned how to train a CNN model from scratch, an essential technique used in machine learning for image recognition and classification. Through this process, we acquired knowledge and expertise in collecting and labelling large datasets, pre-processing image data, and using TensorFlow and Keras to develop and optimise the CNN model's architecture.

Additionally, we learned was how to use Pyqt5, a powerful cross-platform GUI toolkit for Python, to build a user-friendly and responsive website that integrates ASL interpretation functionality.

Moreover, we gained insights into the challenges and nuances associated with developing an ASL interpretation module, including the importance of optimising the model's accuracy and reducing false positives or false negatives, accounting for variations in hand gestures and movements, and addressing technical limitations in capturing and processing live video feeds.

## What's next for SignEase
Expanding the database of an ASL interpretation module to include head gestures and body movements to enhance the accuracy and effectiveness of the technology in interpreting and translating ASL. Incorporating these additional components can improve the context and meaning of the translated text.
By making the ASL interpretation module more inclusive, individuals who use ASL as their primary mode of communication can have greater access to essential services, such as banking and healthcare, and more fully participate in educational and professional settings.

