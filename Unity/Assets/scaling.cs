using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System.Text;

[System.Serializable]
class Coordinates
{
    public int[] Lidar_Location, LidarData_x, LidarData_y;
}
public class scaling : MonoBehaviour
{
    public float speed = 5.0f;
    // Start is called before the first frame update
    public GameObject map;
    public GameObject blockPrefab;

    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetMouseButton(0))
        {
            transform.Rotate(0f, -Input.GetAxis("Mouse X") * speed, 0f, Space.World);
            transform.Rotate(-Input.GetAxis("Mouse Y") * speed, 0f, 0f);
        }
        if(Input.GetKeyDown(KeyCode.Space)){    
            load();
        }
        
    }

    void load()
    {
        string fileName = "test_set";
        string path = Application.dataPath + "/" + fileName + ".json";

        FileStream fileStream = new FileStream(path, FileMode.Open);
        byte[] data = new byte[fileStream.Length];
        fileStream.Read(data, 0, data.Length);
        fileStream.Close();
        string json = Encoding.UTF8.GetString(data);
        Coordinates myCoordinates = JsonUtility.FromJson<Coordinates>(json);

        int[] X = myCoordinates.LidarData_x;
        int[] Y = myCoordinates.LidarData_y;
        int[] machine_coor = myCoordinates.Lidar_Location;
        int length = X.Length;

        GameObject machine = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
        machine.transform.position = new Vector3(machine_coor[0], machine_coor[1]);
        machine.transform.localScale = new Vector3(1f, 0.5f, 1f);
        machine.transform.SetParent(map.transform, false);
        for(int i = 0; i < length; i++)
        {
            make_block(X[i], Y[i]);
        }
        
    }

    void make_block(int x, int y)
    {
        GameObject block = Instantiate(blockPrefab);
        block.transform.position = new Vector3 (x, 0, y);
        block.transform.SetParent(map.transform, false);
    }
}

