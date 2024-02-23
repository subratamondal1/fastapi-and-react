import { useParams } from "react-router-dom";
function ProfilePage() {
  // useParams captures all the parameters available at this route
  const params = useParams();
  return <h1 className="text-2xl">Profile page {params.profileID}</h1>;
}

export default ProfilePage;
