# Music_APi
Music Api using Django Framework


TASK 1 Create a new song

a) So, this image displays the number of songs before adding a new song, that is count = 34.
<img width="1440" alt="Task_1_Before" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/f6ee4104-348c-420b-8d34-01b0fa1f7dbb">

b) Now we add a new song named as "newSong" whose artist is "Jangid". And it also get added successfully. ANd it is also showing the result below that "The song has been created."
<img width="1440" alt="Task_1_Sucess" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/a63406cc-ef99-4b96-a789-b8614b3c9d84">

c) Now lets see the proof whether the song has been created or not. If the song has been created then its count value must have increased by 1.
<img width="1440" alt="Task_1_After" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/d914c587-cf52-4227-aee5-09ac876a4249">

<br>


TASK 2 - LIST AVAILABLE SONGS

a) As you can see it is successfully showing the result of all songs.
<img width="1440" alt="Task_2_part1" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/1b83645e-e8ea-4163-9a36-da708e032c5c">

b) As mentioned in the task that each page should have maximum of 10 songs. This is also done, lets check the below image
<img width="1440" alt="Task_2_part2" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/a4201c41-f677-4c48-ae37-02bb5035e753">

c) We can even access a song using its name by passing a query parameter in url. Lets try to find the song which we have created above in task 1
<img width="1440" alt="Task_2_query_part" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/436d998a-f5b4-435e-9c40-23d669413d7d">
<br>
<br>

TASK 3 - CREATE NEW PLAYLIST

a) Before creating a playlist as you can see in the image below that we have already 15 playlist present in our database
<img width="1440" alt="Task_3_Before" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/6cdf1648-da58-4aff-b008-affa03fbeb75">

b) Now we have created our new playlist. And it is also showing the successful result as "The Playlist Entry has been created".
<img width="1440" alt="task_3_success" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/39ab5000-3cdc-4d66-b180-b4f6b60af3ef">

c) Now you can see the count number has been increased by 1 and our playlist is also there at id = 28.
<img width="1440" alt="Task_3_after" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/5ee540e6-9433-4659-b774-81b0b9b015a6">


TASK 4 - LIST AVAILABLE PLAYLIST

a) We can acess the list of all playlist as shown below and it will aslo the link to next page because we have total of 16 playlist in our database and they have asked us to print only 10 in one page.
<img width="1440" alt="Task_4_part1" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/86141666-9ca9-4961-b332-a9b9990be8da">

b) We can even acess the particular playlist my mentioning its name in the query parameter in the url as shown below, we have fetch the playlist which we have created in the above task.
<img width="1440" alt="Task_4_part2" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/2d7f4cb1-0b5a-4504-8a29-8e5ee8c3602d">



TASK 5 - EDIT PLAYLIST METADATA

a) As the id = 28 was there for playlist we have created above, so here we have successfully updated the name of our playlist. And it is also showing that the "The name of the playlist has been chnaged"
<img width="1440" alt="Task_5_Success" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/4df53184-b652-4a4e-a1b6-c84018edd2a8">

b) As a proof we can see that at same idea now we have a playlist of updated name.
<img width="1440" alt="Task_5_proof" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/06ba0717-90dc-4fb3-8029-151ec680bb0d">


TASK 6 - DELETE PLAYLIST

a) Now we have deleted the same playlist which we have created by using its "id" in the url. And we also got the successful message as "The playlist has been deleted"
<img width="1440" alt="Task_6_success" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/9dc3607f-8204-4b47-8dd0-1c7ef9610023">

b) As a proof we can even see that now the count of playlist has also become 15.
<img width="1440" alt="Task_6_proof" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/604108fb-eb2f-4317-93b4-89af7f285ac8">



TASK 7 - LIST PLAYLIST SONGS

a) Here we shown all the songs presesnt in the playlist having id = 21
<img width="1440" alt="Task_7" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/e19954cc-f4e6-46ee-80e2-8c0b6cbcee86">


TASK 8 - MOVE PLAYLIST SONG

a) As you can see in the above mentioned playlist with id = 21 has a song named as "song1" at position 2 and has a id = 62. So, now we will try to chnage its position to 1 by passing the playlist id and song id in url and passing the position value as 1.
It is also showing the successfull result as that "The song has been moved to the new position in the playlist"
<img width="1440" alt="task_8_Success" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/ad56bfae-5cdb-4e38-9bfa-67ecfda0ca77">

b) Lets see the proof 
<img width="1440" alt="TAsk_8_Proof" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/20ca1783-e8d1-45d0-b8e5-96a736fa9cba">


TASK 9 - REMOVE PLAYLIST SONG

a) Now we will remove the same song the same playlist as discuussed in above task
And it is also showing result as "The song has been deleted"
<img width="1440" alt="Task_9_Success" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/c3830017-4f2b-45a0-9321-91e1c05f5484">

b) Lets see the proof beacuse as that song was at position 1 earlier now after deletion of that song would some other song to raech at position 1, mainly the song who was at position 2 now has reached to position 1.
<img width="1440" alt="Task_9_Proof" src="https://github.com/deepakJangidz/Music_APi/assets/162096851/0ee05aca-0d2e-477e-8819-a1c071912ec7">


THANKYOU 
ALL TASKS HAS BEEN COMPLETED SUCCESSFULLY.

















